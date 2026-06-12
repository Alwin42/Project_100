const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
    vendorId: { 
        type: mongoose.Schema.Types.ObjectId, 
        ref: 'User', 
        required: true 
    },
    name: { type: String, required: true },
    category: { type: String, required: true },
    price: { type: Number, required: true },
    unit: { type: String, required: true },
    inStock: { type: Boolean, default: true },
    emoji: { type: String, default: '📦' }
}, { timestamps: true });

module.exports = mongoose.model('Product', productSchema);