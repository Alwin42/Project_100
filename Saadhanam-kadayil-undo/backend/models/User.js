const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true, lowercase: true, trim: true },
    role: { type: String, enum: ['customer', 'vendor'], default: 'customer' },
    isOpen: { type: Boolean, default: true },
    openTime: { type: String, default: '08:00' },  
    closeTime: { type: String, default: '21:00' }, 
    shopName: { type: String },
    ownerName: { type: String },
    phone: { type: String },
    address: { type: String },
    mapUrl: { type: String },
    password: { type: String }, 
    lastLogin: { type: Date, default: Date.now }
}, { timestamps: true });

module.exports = mongoose.model('User', userSchema);