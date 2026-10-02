# 🛠️ Loco - Local Service Provider Platform

**Loco** is a modern, lightweight web application designed to connect local service providers (plumbers, electricians, tutors, cleaners, etc.) with customers in their area. Built with a high-performance, decoupled architecture, it offers a seamless experience for booking, managing, and reviewing local services.

---

## 🚀 Tech Stack

### Frontend
- **Vue.js 3** (Composition API)
- **Vite** (Build tool)
- **Tailwind CSS v4** (Styling)
- **Pinia** (State Management)
- **Vue Router** (Routing)
- **Axios** (HTTP Client)

### Backend
- **FastAPI** (High-performance Python web framework)
- **SQLAlchemy** (ORM)
- **SQLite3** (Lightweight database, easily upgradable to PostgreSQL)
- **Pydantic** (Data validation)
- **Passlib & Python-Jose** (JWT Authentication & Password Hashing)

---

## ✨ Core Features

### 👤 For Customers
- Browse and search service providers by category and location.
- View detailed provider profiles, services, and ratings.
- Book appointments and manage booking history.
- Leave reviews and ratings for completed services.

### 🛠️ For Service Providers
- Create and manage a business profile.
- List services with custom pricing and duration.
- Accept, manage, and track booking requests.
- View basic analytics and earnings.

### 🛡️ For Admins
- User and provider verification management.
- Category and platform-wide settings.
- Review moderation.

---

## 📁 Project Structure

```text
Project_100/
├── Loco/
│   ├── backend/                 # FastAPI Backend
│   │   ├── app/
│   │   │   ├── main.py          # App entry point
│   │   │   ├── database.py      # SQLite connection setup
│   │   │   ├── models.py        # SQLAlchemy database models
│   │   │   ├── schemas.py       # Pydantic validation schemas
│   │   │   ├── routers/         # API route handlers (auth, users, bookings, etc.)
│   │   │   ├── crud.py          # Database operations
│   │   │   └── security.py      # JWT & password hashing utilities
│   │   ├── requirements.txt     # Python dependencies
│   │   └── .env                 # Environment variables (not committed)
│   │
│   └── frontend/                # Vue.js Frontend
│       ├── src/
│       │   ├── assets/          # Global CSS (Tailwind v4 entry)
│       │   ├── components/      # Reusable UI components
│       │   ├── views/           # Page-level components
│       │   ├── router/          # Vue Router configuration
│       │   ├── stores/          # Pinia state management
│       │   └── main.js          # Vue app entry point
│       ├── vite.config.js       # Vite config (includes Tailwind v4 plugin)
│       └── package.json         # Node dependencies
│
└── README.md