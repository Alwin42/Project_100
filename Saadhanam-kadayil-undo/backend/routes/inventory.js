const Order = require('../models/Order'); // Add this import at the very top of the file!

// GET: Fetch Active Orders for a Vendor
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