const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
    vendorId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    customerName: { type: String, default: 'Customer' },
    
    //  save the exact item being reserved!
    item: {
        productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product', required: true },
        name: { type: String, required: true },
        price: { type: String, required: true },
        emoji: { type: String }
    },
    
    status: { type: String, default: 'Pending' } // Pending, Accepted, Declined
}, { timestamps: true });

module.exports = mongoose.model('Order', orderSchema);