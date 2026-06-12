const express = require('express');
const User = require('../models/User'); 
const Product = require('../models/Product'); 
const router = express.Router();

// GET: Fetch all registered vendors
router.get('/vendors', async (req, res) => {
    try {
        const vendors = await User.find({ role: 'vendor' })
    .select('shopName mapUrl address isOpen openTime closeTime');
        res.status(200).json({ success: true, vendors });
    } catch (error) {
        console.error("Fetch Vendors Error:", error);
        res.status(500).json({ error: "Failed to fetch vendors." });
    }
});

// GET: Fetch ALL active items across ALL stores
router.get('/items', async (req, res) => {
    try {
        // Find all items in stock
        // .populate() reaches into the User collection and grabs the shopName!
        const items = await Product.find()
            .populate('vendorId', 'shopName') 
            .sort({ createdAt: -1 })
            .limit(20); // Optional: Limit to newest 20 items so the page doesn't lag
        
        res.status(200).json({ success: true, items });
    } catch (error) {
        console.error("Fetch Items Error:", error);
        res.status(500).json({ error: "Failed to fetch items." });
    }
});

module.exports = router;