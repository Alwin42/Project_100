// 1. Load environment variables IMMEDIATELY (Must be the very first line)
require('dotenv').config();

const express = require('express');
const cors = require('cors');

// 2. Import the auth routes we built earlier
// (Make sure the path matches where you saved your auth.js file)
const authRoutes = require('./routes/auth'); 

const app = express();

// 3. Middleware
app.use(cors()); // Allows your Vue frontend (localhost:5173) to talk to this server
app.use(express.json()); // Tells Express to parse incoming JSON data (like your email and OTP)

// 4. Mount the Routes
// Every route inside auth.js will now start with /api/auth
app.use('/api/auth', authRoutes);

// 5. Health Check Route (Crucial for Render)
// Render will ping this URL to make sure your server successfully booted up
app.get('/', (req, res) => {
    res.status(200).json({ message: " Backend is live and running!" });
});

// 6. Start the Server
// Render automatically provides process.env.PORT. If running locally, it defaults to 3000.
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`🚀 Server is up and running on port http://localhost:${PORT}`);
});