# Meat-Undo 🥩

Meat-Undo (powered by StockUndo) is a modern, full-stack local meat, poultry, and seafood ordering platform. It bridges the gap between local butchers/fishmongers and nearby customers, allowing shop owners to manage their highly-perishable live inventory while customers can discover, order, and reserve specific cuts in real-time.

---

## ✨ Features

### 🏪 For Vendors
* **Secure Authentication:** Register and login via JWT and securely hashed passwords.
* **Interactive Dashboard:** View real-time stats, expected revenue, platform fees, and active orders.
* **Live Inventory Management:** Add, edit, delete, and instantly toggle stock status (In Stock / Out of Stock) for specific cuts and products.
* **Order Management:** Accept or decline pending customer orders on the fly.
* **Delivery Flexibility:** Toggle between "Pickup Only" and "Home Delivery" modes.

### 👤 For Customers
* **Passwordless Login:** Frictionless authentication using email OTPs powered by the Brevo REST API.
* **Vendor Discovery:** Find nearby open butchers and fishmongers and view their map locations.
* **Smart Search:** Quickly search for specific fresh cuts or seafood across all nearby vendors before walking out the door.

---

## 🛠️ Tech Stack

**Frontend (Client)**
* **Framework:** Vue 3 (Composition API / `<script setup>`)
* **Styling:** Tailwind CSS v4 (Animations, interactive hover states, modern rounded-4xl design)
* **Routing:** Vue Router
* **HTTP Client:** Axios
* **Icons:** Lucide-Vue-Next

**Backend (Server)**
* **Runtime:** Node.js
* **Framework:** Express.js
* **Database:** MongoDB (via Mongoose)
* **Authentication:** JSON Web Tokens (JWT) & bcryptjs
* **Email Service:** Brevo (via secure REST API, no SMTP required)

---

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
* [Node.js](https://nodejs.org/) (v16 or higher)
* A [MongoDB Atlas](https://www.mongodb.com/atlas) account (or local MongoDB server)
* A [Brevo](https://www.brevo.com/) account for the API Key

### 1. Clone the Repository
*Note: Because this project is part of a larger monorepo, you will clone the main repository and navigate to the project folder.*
```bash
git clone [https://github.com/Alwin42/Project_100.git](https://github.com/Alwin42/Project_100.git)
cd Project_100/Meat-Undo