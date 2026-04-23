require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose'); // 1. Import Mongoose

const authRoutes = require('./routes/auth'); 

const app = express();

app.use(cors()); 
app.use(express.json()); 

app.use('/api/auth', authRoutes);

app.get('/', (req, res) => {
    res.status(200).json({ message: "StockUndo Backend is live!" });
});

// 2. Connect to MongoDB Atlas
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('📦 Connected to MongoDB Atlas Successfully!'))
  .catch((err) => console.error('MongoDB Connection Error:', err));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
});