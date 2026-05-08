# Saadhanam Kadayil undo

Saadhanam Kadayil undo aka StockUndo is a modern, full-stack local grocery ordering and inventory management platform. It bridges the gap between local vendors and nearby customers, allowing shop owners to manage their live inventory while customers can discover and reserve items in real-time.

---

## ✨ Features

### 🏪 For Vendors
* **Secure Authentication:** Register and login via JWT and securely hashed passwords.
* **Interactive Dashboard:** View real-time stats, today's revenue, and active orders.
* **Live Inventory Management:** Add, edit, delete, and instantly toggle stock status (In Stock / Out of Stock) for products.
* **Order Management:** Accept or decline pending customer orders.

### 👤 For Customers
* **Passwordless Login:** Frictionless authentication using email OTPs powered by the Brevo REST API.
* **Vendor Discovery:** Find nearby open stores and view their map locations.
* **Smart Search:** Quickly search for specific grocery items across all nearby vendors.

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
```bash
git clone [https://github.com/Alwin42/Project_100/tree/main/Saadhanam-kadayil-undo](https://github.com/Alwin42/Project_100/tree/main/Saadhanam-kadayil-undo)
cd Saadhanam-kadayil-undo