const express = require('express');
const jwt = require('jsonwebtoken');
const Product = require('../models/Product');
const Order = require('../models/Order'); // Make sure this model exists too!
const router = express.Router();

// SECURITY MIDDLEWARE
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

// POST: Add a new item
router.post('/add', authenticateToken, async (req, res) => {
    try {
        const { name, category, price, unit, inStock } = req.body;
        const newProduct = new Product({
            vendorId: req.user.userId,
            name, category, price, unit, inStock
        });
        await newProduct.save();
        res.status(201).json({ success: true, product: newProduct });
    } catch (error) {
        res.status(500).json({ error: "Failed to add product." });
    }
});

// GET: Fetch all items for the logged-in vendor
router.get('/', authenticateToken, async (req, res) => {
    try {
        const products = await Product.find({ vendorId: req.user.userId }).sort({ createdAt: -1 });
        res.status(200).json({ success: true, products });
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch products." });
    }
});

// GET: Fetch Active Orders
router.get('/orders', authenticateToken, async (req, res) => {
    try {
        const orders = await Order.find({ 
            vendorId: req.user.userId,
            status: 'Pending' 
        }).sort({ createdAt: -1 });
        res.status(200).json({ success: true, orders });
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch orders." });
    }
});
// PUT: Update an existing item (Edit & Toggle Stock)
router.put('/update/:id', authenticateToken, async (req, res) => {
    try {
        const updatedProduct = await Product.findOneAndUpdate(
            { _id: req.params.id, vendorId: req.user.userId }, 
            req.body, 
            { new: true } // Returns the updated document
        );
        if (!updatedProduct) return res.status(404).json({ error: "Product not found" });
        res.status(200).json({ success: true, product: updatedProduct });
    } catch (error) {
        res.status(500).json({ error: "Failed to update product." });
    }
});

// DELETE: Remove an item
router.delete('/delete/:id', authenticateToken, async (req, res) => {
    try {
        const deletedProduct = await Product.findOneAndDelete({ 
            _id: req.params.id, 
            vendorId: req.user.userId 
        });
        if (!deletedProduct) return res.status(404).json({ error: "Product not found" });
        res.status(200).json({ success: true, message: "Product deleted" });
    } catch (error) {
        res.status(500).json({ error: "Failed to delete product." });
    }
});
module.exports = router;