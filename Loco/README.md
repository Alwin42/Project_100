# 🛠️ Loco - Local Service Provider Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vue.js&logoColor=white)](https://vuejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

**Loco** is a modern, high-performance web application designed to seamlessly connect local service providers (plumbers, electricians, tutors, cleaners, etc.) with customers in their area. Built with a decoupled, API-first architecture, it offers a robust and intuitive platform for discovering, booking, and managing local services.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Core Features](#-core-features)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🌟 Overview
Finding reliable local help shouldn't be a hassle. Loco bridges the gap between skilled local professionals and customers who need their services. Whether you need an emergency pipe repair, a deep home cleaning, or a math tutor, Loco provides a verified, transparent, and easy-to-use marketplace.

---

## 💻 Tech Stack

### Frontend
| Technology | Purpose |
| :--- | :--- |
| **Vue.js 3** | Progressive JavaScript framework (Composition API) |
| **Vite** | Next-generation frontend build tool |
| **Tailwind CSS v4** | Utility-first CSS framework for rapid UI development |
| **Vue Router** | Official routing library for Single Page Applications |
| **Pinia** | Intuitive, type-safe state management |
| **Axios** | Promise-based HTTP client for API communication |
| **Lucide** | Beautiful & consistent open-source icons |

### Backend
| Technology | Purpose |
| :--- | :--- |
| **FastAPI** | Modern, high-performance Python web framework |
| **SQLAlchemy** | Python SQL toolkit and Object Relational Mapper (ORM) |
| **SQLite3** | Lightweight, serverless relational database |
| **Pydantic** | Data validation and settings management using Python type annotations |
| **Bcrypt & Python-Jose** | Secure password hashing and JWT authentication |

---

## ✨ Core Features

### 👤 For Customers
- **Smart Discovery:** Browse and search service providers by category, location, and ratings.
- **Transparent Profiles:** View detailed provider profiles, portfolios, and verified customer reviews.
- **Seamless Booking:** Book appointments instantly and manage your booking history.
- **Feedback Loop:** Leave reviews and ratings for completed services to help the community.

### 🛠️ For Service Providers
- **Business Management:** Create and manage a comprehensive business profile.
- **Service Catalog:** List services with custom pricing, descriptions, and durations.
- **Booking Control:** Accept, manage, and track incoming booking requests.
- **Performance Tracking:** View basic analytics, completed jobs, and earnings.

### 🛡️ For Admins
- **Verification:** Manage user and provider verification workflows.
- **Platform Control:** Manage service categories and platform-wide settings.
- **Quality Assurance:** Moderate reviews and handle dispute resolutions.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed on your machine:
- **Python** 3.10 or higher
- **Node.js** 18 or higher & **npm**

### 1. Backend Setup
```bash
# Navigate to the backend directory
cd Loco/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI development server
uvicorn app.main:app --reload