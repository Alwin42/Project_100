const express = require('express');
const axios = require('axios'); 
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const User = require('../models/User'); 
const router = express.Router();

const otpStore = {}; 

// --- SECURITY MIDDLEWARE ---
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) return res.status(401).json({ error: "Access denied. No token provided." });

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: "Invalid or expired token." });
        req.user = user; 
        next();
    });
};

// --- 1. CUSTOMER OTP ENDPOINTS ---
router.post('/send-otp', async (req, res) => {
    const { email } = req.body;
    if (!email) return res.status(400).json({ error: "Email is required" });

    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    otpStore[email] = { otp, expiresAt: Date.now() + 5 * 60 * 1000 };

    try {
        await axios.post('https://api.brevo.com/v3/smtp/email', {
            sender: { name: "StockUndo", email: "alwindev1010@gmail.com" }, 
            to: [{ email: email }],
            subject: "Your StockUndo Login Code",
            htmlContent: `
                <div style="font-family: Arial, sans-serif; text-align: center; padding: 20px;">
                    <h2>Welcome to StockUndo!</h2>
                    <p>Your secure login code is:</p>
                    <h1 style="color: #2b7a0b; font-size: 40px; letter-spacing: 5px;">${otp}</h1>
                    <p style="color: #666; font-size: 12px;">This code expires in 5 minutes.</p>
                </div>
            `
        }, {
            headers: {
                'api-key': process.env.BREVO_API_KEY, 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
        res.status(200).json({ success: true, message: "OTP sent!" });
    } catch (error) {
        res.status(500).json({ error: "Failed to send OTP email." });
    }
});

router.post('/verify-otp', async (req, res) => {
    const { email, otp } = req.body;
    const record = otpStore[email];

    if (!record || record.expiresAt < Date.now()) return res.status(400).json({ error: "OTP expired or invalid" });

    if (record.otp === otp) {
        delete otpStore[email]; 
        try {
            let user = await User.findOne({ email: email.toLowerCase() });
            if (user) {
                user.lastLogin = Date.now();
                await user.save();
            } else {
                user = new User({ email: email.toLowerCase(), role: 'customer' });
                await user.save();
            }

            const token = jwt.sign(
                { userId: user._id, email: user.email, role: user.role }, 
                process.env.JWT_SECRET, 
                { expiresIn: '7d' }
            );
            return res.status(200).json({ success: true, token, role: user.role, message: "Login successful!" });
        } catch (error) {
            return res.status(500).json({ error: "Database error during login." });
        }
    } else {
        return res.status(400).json({ error: "Incorrect OTP" });
    }
});

// --- 2. VENDOR REGISTRATION ---
router.post('/vendor/register', async (req, res) => {
    const { shopName, ownerName, email, phone, address, mapUrl, password } = req.body;
    try {
        const existingUser = await User.findOne({ email: email.toLowerCase() });
        if (existingUser) return res.status(400).json({ error: "Email is already registered." });

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newVendor = new User({
            email: email.toLowerCase(),
            role: 'vendor',
            shopName, ownerName, phone, address, mapUrl,
            password: hashedPassword
        });
        await newVendor.save();

        const token = jwt.sign(
            { userId: newVendor._id, email: newVendor.email, role: newVendor.role },
            process.env.JWT_SECRET, { expiresIn: '7d' }
        );
        res.status(201).json({ success: true, token, role: newVendor.role, message: "Vendor registered successfully!" });
    } catch (error) {
        res.status(500).json({ error: "Server error during registration." });
    }
});

// --- 3. VENDOR LOGIN ---
router.post('/vendor/login', async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await User.findOne({ email: email.toLowerCase(), role: 'vendor' });
        if (!user) return res.status(400).json({ error: "Invalid credentials." });

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) return res.status(400).json({ error: "Invalid credentials." });

        user.lastLogin = Date.now();
        await user.save();

        const token = jwt.sign(
            { userId: user._id, email: user.email, role: user.role, shopName: user.shopName },
            process.env.JWT_SECRET, { expiresIn: '7d' }
        );
        res.status(200).json({ success: true, token, role: user.role, message: "Login successful!" });
    } catch (error) {
        res.status(500).json({ error: "Server error during login." });
    }
});

// --- 4. GET VENDOR SETTINGS (OPEN/CLOSE STATUS) ---
router.get('/vendor/settings', authenticateToken, async (req, res) => {
    try {
        const user = await User.findById(req.user.userId);
        if (!user) return res.status(404).json({ error: "User not found." });
        res.status(200).json({ success: true, isOpen: user.isOpen ?? true });
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch shop settings." });
    }
});

// --- 5. PUT VENDOR SETTINGS (OPEN/CLOSE STATUS) ---
router.put('/vendor/settings', authenticateToken, async (req, res) => {
    try {
        const { isOpen } = req.body;
       const updatedUser = await User.findByIdAndUpdate(
       req.user.userId, 
       { isOpen: isOpen }, 
       { returnDocument: 'after' } 
        );
        if (!updatedUser) return res.status(404).json({ error: "User not found." });
        res.status(200).json({ success: true, isOpen: updatedUser.isOpen });
    } catch (error) {
        res.status(500).json({ error: "Failed to update shop settings." });
    }
});


module.exports = router;