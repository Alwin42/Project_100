require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth'); 
const publicRoutes = require('./routes/public');
const inventoryRoutes = require('./routes/inventory'); 
const orderRoutes = require('./routes/orders');
const app = express();

app.use(cors()); 
app.use(express.json()); 

// 2. TELL EXPRESS TO USE YOUR ROUTES
app.use('/api/auth', authRoutes);
app.use('/api/public', publicRoutes);
app.use('/api/inventory', inventoryRoutes);
app.use('/api/orders', orderRoutes);
app.get('/', (req, res) => {
    res.status(200).json({ message: "StockUndo Backend is live!" });
});

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('📦 Connected to MongoDB Atlas Successfully!'))
  .catch((err) => console.error('MongoDB Connection Error:', err));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
});