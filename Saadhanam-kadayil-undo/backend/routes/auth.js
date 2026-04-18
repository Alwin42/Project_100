// backend/routes/auth.js
const express = require('express');
const nodemailer = require('nodemailer');
const jwt = require('jsonwebtoken');
const router = express.Router();

const otpStore = {}; 

// 1. Configure Nodemailer with Brevo (Sendinblue) SMTP settings
const transporter = nodemailer.createTransport({
    host: 'smtp-relay.brevo.com',
    port: 587,
    secure: false, // true for 465, false for 587
    auth: {
        user: process.env.BREVO_SMTP_LOGIN, // Usually your Brevo account email
        pass: process.env.BREVO_SMTP_KEY    // Generate this in Brevo: SMTP & API -> SMTP
    }
});

// 2. Endpoint to Request Email OTP
router.post('/send-otp', async (req, res) => {
    const { email } = req.body;

    if (!email) {
        return res.status(400).json({ error: "Email address is required" });
    }

    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    otpStore[email] = { otp, expiresAt: Date.now() + 5 * 60 * 1000 };

    try {
        // Send the email via Brevo
        await transporter.sendMail({
            from: '"StockUndo" <noreply@yourdomain.com>', // Replace with your verified Brevo sender email
            to: email,
            subject: "Your StockUndo Login Code",
            html: `
                <div style="font-family: sans-serif; text-align: center; padding: 20px;">
                    <h2>Welcome to StockUndo!</h2>
                    <p>Your one-time login code is:</p>
                    <h1 style="letter-spacing: 5px; color: #16a34a;">${otp}</h1>
                    <p style="color: #666; font-size: 12px;">This code expires in 5 minutes.</p>
                </div>
            `
        });

        console.log(`Email OTP ${otp} sent to ${email}`);
        res.status(200).json({ success: true, message: "OTP sent to email" });

    } catch (error) {
        console.error("Brevo SMTP Error:", error);
        res.status(500).json({ error: "Failed to send email. Please try again." });
    }
});

// 3. Endpoint to Verify OTP
router.post('/verify-otp', async (req, res) => {
    const { email, otp } = req.body;
    const record = otpStore[email];

    if (!record || record.expiresAt < Date.now()) {
        return res.status(400).json({ error: "OTP expired or invalid" });
    }

    if (record.otp === otp) {
        delete otpStore[email]; // Clear OTP after success
        
        // Generate session token
        const token = jwt.sign({ email }, process.env.JWT_SECRET || 'supersecret', { expiresIn: '7d' });

        return res.status(200).json({ success: true, token, message: "Login successful!" });
    } else {
        return res.status(400).json({ error: "Incorrect OTP" });
    }
});

module.exports = router;