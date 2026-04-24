const express = require('express');
const nodemailer = require('nodemailer');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs'); // Import bcrypt for password hashing
const User = require('../models/User'); // Import your new DB Model
const router = express.Router();

const otpStore = {}; 

const transporter = nodemailer.createTransport({
    host: 'smtp-relay.brevo.com',
    port: 587,
    secure: false, 
    auth: {
        user: process.env.BREVO_SMTP_LOGIN, 
        pass: process.env.BREVO_SMTP_KEY    
    }
});

// --- 1. CUSTOMER OTP ENDPOINTS ---
router.post('/send-otp', async (req, res) => {
    // ... (Keep your existing send-otp logic exactly as it is)
});

router.post('/verify-otp', async (req, res) => {
    const { email, otp } = req.body;
    const record = otpStore[email];

    if (!record || record.expiresAt < Date.now()) return res.status(400).json({ error: "OTP expired or invalid" });

    if (record.otp === otp) {
        delete otpStore[email]; 
        try {
            // Find or create the customer in the database
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
        // 1. Check if email already exists
        const existingUser = await User.findOne({ email: email.toLowerCase() });
        if (existingUser) {
            return res.status(400).json({ error: "Email is already registered." });
        }

        // 2. Hash the password securely
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        // 3. Save the new Vendor to MongoDB
        const newVendor = new User({
            email: email.toLowerCase(),
            role: 'vendor', // Explicitly set role to vendor
            shopName,
            ownerName,
            phone,
            address,
            mapUrl,
            password: hashedPassword
        });

        await newVendor.save();

        // 4. Generate a JWT token so they log in instantly upon registering
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
        // 1. Find the user by email AND ensure they are a vendor
        const user = await User.findOne({ email: email.toLowerCase(), role: 'vendor' });
        
        if (!user) {
            return res.status(400).json({ error: "Invalid credentials or not a vendor account." });
        }

        // 2. Compare the provided password with the hashed password in the database
        const isMatch = await bcrypt.compare(password, user.password);
        
        if (!isMatch) {
            return res.status(400).json({ error: "Invalid credentials." });
        }

        // 3. Update their last login time
        user.lastLogin = Date.now();
        await user.save();

        // 4. Generate the secure JWT
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