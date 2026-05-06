const express = require('express');
const User = require('../models/User'); 
const router = express.Router();

// Fetch all registered vendors
router.get('/vendors', async (req, res) => {
    try {
        // Find all users where role is 'vendor'
        // .select() ensures we don't accidentally send passwords to the frontend!
        const vendors = await User.find({ role: 'vendor' }).select('shopName mapUrl address');
        
        res.status(200).json({ success: true, vendors });
    } catch (error) {
        console.error("Fetch Vendors Error:", error);
        res.status(500).json({ error: "Failed to fetch vendors." });
    }
});

module.exports = router;