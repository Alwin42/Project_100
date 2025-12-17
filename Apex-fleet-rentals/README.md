Here is a professional **README.md** file for your project. You should save this in the root folder `Apex-fleet-rentals/`.

This document serves as the central documentation for your project, explaining how to run both the Django backend and the Vue frontend.

---

# Apex Fleet Rentals

**Apex Fleet Rentals** is a comprehensive car rental management system designed to streamline vehicle bookings, fleet management, and customer interactions. It features a modern, responsive frontend and a robust, scalable backend API.

## 🛠 Tech Stack

### Frontend

* **Framework:** Vue.js 3 (Composition API)
* **Styling:** Tailwind CSS
* **State Management:** Pinia
* **Routing:** Vue Router
* **Build Tool:** Vite

### Backend

* **Framework:** Django 5
* **API:** Django REST Framework (DRF)
* **Database:** SQLite (Dev) / PostgreSQL (Prod)
* **Authentication:** JWT (JSON Web Tokens)

---

## 📂 Project Structure

```text
Apex-fleet-rentals/
├── backend/            # Django Project (API & Admin)
│   ├── core/           # Project settings
│   ├── fleet/          # Main app logic (cars, bookings)
│   ├── manage.py
│   └── venv/           # Python Virtual Environment
├── frontend/           # Vue.js Project (Client-side)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── tailwind.config.js
└── README.md

```

---

## 🚀 Getting Started

Follow these steps to set up the development environment on your local machine.

### Prerequisites

* **Python** (3.10+)
* **Node.js** (LTS version) & **npm**

### 1. Backend Setup (Django)

Navigate to the backend directory and set up the virtual environment.

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate
# Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers Pillow

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver

```

*The Backend API will run at `http://127.0.0.1:8000/*`

### 2. Frontend Setup (Vue.js)

Open a new terminal, navigate to the frontend directory, and install dependencies.

```bash
cd frontend

# Install Node modules
npm install

# Run the development server
npm run dev

```

*The Frontend will run at `http://localhost:5173/*`

---

## ✨ Features (Planned)

* **User Roles:** Distinct dashboards for Guests, Customers, and Admins.
* **Fleet Inventory:** detailed vehicle listings with images, specs, and availability status.
* **Booking Engine:** Date-based reservation system with conflict detection.
* **Dynamic Pricing:** Automated calculation of rental costs based on duration.

---

## 📝 Future Roadmap

* **Payment Gateway:** Integration with Stripe/PayPal.
* **Map Integration:** Visual pickup/drop-off locations.
* **Notifications:** Email/SMS updates for booking confirmations (using Celery/Redis).

---

### **Next Step**

You currently have the basic Vue installation. We still need to **configure Tailwind CSS** for the frontend to match your requirement.

**Would you like the commands to finish the Tailwind setup now?**