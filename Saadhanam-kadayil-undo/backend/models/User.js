const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true, lowercase: true, trim: true },
    role: { type: String, enum: ['customer', 'vendor'], default: 'customer' },
    
    // Vendor-specific fields (These align perfectly with your frontend form)
    shopName: { type: String },
    ownerName: { type: String },
    phone: { type: String },
    address: { type: String },
    mapUrl: { type: String },
    password: { type: String }, // Only vendors will have this
    
    lastLogin: { type: Date, default: Date.now }
}, { timestamps: true });

module.exports = mongoose.model('User', userSchema);