const express = require('express');
const jwt = require('jsonwebtoken');
const Order = require('../models/Order');
const Product = require('../models/Product');
const router = express.Router();

// Middleware to check if user is logged in
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if (!token) return res.status(401).json({ error: "Please login to continue." });

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: "Session expired. Please login again." });
        req.user = user; 
        next();
    });
};

// 1. CUSTOMER: Reserve an Item
router.post('/reserve', authenticateToken, async (req, res) => {
    try {
        const { productId } = req.body;

        // Step A: Find the product and check if it exists
        const product = await Product.findById(productId);
        if (!product) return res.status(404).json({ error: "Item not found." });

        // Step B: CRITICAL SYNC CHECK - Is it actually in stock?
        if (!product.inStock) {
            return res.status(400).json({ error: "Sorry, this item just went out of stock!" });
        }

        // Step C: Create the reservation
        const newOrder = new Order({
            vendorId: product.vendorId,
            customerId: req.user.userId,
            customerName: req.user.email.split('@')[0], // Uses the first part of their email as a name
            item: {
                productId: product._id,
                name: product.name,
                price: product.price,
                emoji: product.emoji
            }
        });

        await newOrder.save();
        res.status(201).json({ success: true, message: "Item reserved successfully!", order: newOrder });

    } catch (error) {
        console.error("Reservation Error:", error);
        res.status(500).json({ error: "Failed to reserve item." });
    }
});

// 2. VENDOR: Update Order Status (Accept/Decline)
router.put('/status/:orderId', authenticateToken, async (req, res) => {
    try {
        const { status } = req.body; // 'Accepted' or 'Declined'
        
        // Find the order and ensure it belongs to the logged-in vendor
        const order = await Order.findOneAndUpdate(
            { _id: req.params.orderId, vendorId: req.user.userId },
            { status: status },
            { new: true }
        );

        if (!order) return res.status(404).json({ error: "Order not found." });
        res.status(200).json({ success: true, order });

    } catch (error) {
        res.status(500).json({ error: "Failed to update order." });
    }
});

module.exports = router;