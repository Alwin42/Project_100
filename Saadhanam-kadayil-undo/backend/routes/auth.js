const express = require('express');
const axios = require('axios'); // Replaced nodemailer with axios
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const User = require('../models/User'); 
const router = express.Router();

// Temporary in-memory store for OTPs (For production later, consider Redis or MongoDB)
const otpStore = {}; 

// --- 1. CUSTOMER OTP ENDPOINTS ---
router.post('/send-otp', async (req, res) => {
    const { email } = req.body;

    if (!email) {
        return res.status(400).json({ error: "Email is required" });
    }

    // Generate a 4-digit OTP
    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    
    // Store OTP with a 5-minute expiration
    otpStore[email] = { 
        otp, 
        expiresAt: Date.now() + 5 * 60 * 1000 
    };

    try {
        // FAST REST API CALL TO BREVO (No SMTP handshake required)
        await axios.post('https://api.brevo.com/v3/smtp/email', {
            sender: { name: "StockUndo", email: "alwindev1010@gmail.com" }, // Change email if needed
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
                'api-key': process.env.BREVO_API_KEY, // Uses API key instead of SMTP credentials
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });

        res.status(200).json({ success: true, message: "OTP sent rapidly via API!" });
    } catch (error) {
        console.error("Brevo API Error:", error.response?.data || error.message);
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

// --- 2. VENDOR REGISTRATION ENDPOINT ---
router.post('/vendor/register', async (req, res) => {
    const { shopName, ownerName, email, phone, address, mapUrl, password } = req.body;

    try {
        const existingUser = await User.findOne({ email: email.toLowerCase() });
        if (existingUser) {
            return res.status(400).json({ error: "Email is already registered." });
        }

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newVendor = new User({
            email: email.toLowerCase(),
            role: 'vendor',
            shopName,
            ownerName,
            phone,
            address,
            mapUrl,
            password: hashedPassword
        });

        await newVendor.save();

        const token = jwt.sign(
            { userId: newVendor._id, email: newVendor.email, role: newVendor.role },
            process.env.JWT_SECRET,
            { expiresIn: '7d' }
        );

        res.status(201).json({ success: true, token, role: newVendor.role, message: "Vendor registered successfully!" });

    } catch (error) {
        console.error("Vendor Registration Error:", error);
        res.status(500).json({ error: "Server error during registration." });
    }
});

// --- 3. VENDOR LOGIN ENDPOINT ---
router.post('/vendor/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        const user = await User.findOne({ email: email.toLowerCase(), role: 'vendor' });
        
        if (!user) {
            return res.status(400).json({ error: "Invalid credentials or not a vendor account." });
        }

        const isMatch = await bcrypt.compare(password, user.password);
        
        if (!isMatch) {
            return res.status(400).json({ error: "Invalid credentials." });
        }

        user.lastLogin = Date.now();
        await user.save();

        const token = jwt.sign(
            { 
              userId: user._id, 
              email: user.email, 
              role: user.role,
              shopName: user.shopName 
            },
            process.env.JWT_SECRET,
            { expiresIn: '7d' }
        );

        res.status(200).json({ success: true, token, role: user.role, message: "Vendor login successful!" });

    } catch (error) {
        console.error("Vendor Login Error:", error);
        res.status(500).json({ error: "Server error during login." });
    }
});

module.exports = router;