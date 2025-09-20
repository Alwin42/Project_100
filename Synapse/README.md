# Synapse - Unified Booking System

A comprehensive booking system designed to connect hospitals and laboratories in a neighborhood, making healthcare more accessible and efficient for patients.

## 🏥 About

Synapse is a unified booking platform that bridges the gap between healthcare providers and patients by connecting multiple hospitals and laboratories in a local area. The system enables patients to easily find, compare, and book appointments across different healthcare facilities, streamlining the healthcare experience.

## ✨ Features

- **Multi-facility Integration** - Connect multiple hospitals and laboratories in one platform
- **Unified Booking System** - Book appointments across different healthcare providers
- **Patient-Centric Design** - Easy-to-use interface for patients to manage their healthcare needs
- **Neighborhood Network** - Focused on local healthcare providers for community convenience
- **Real-time Availability** - Check and book available slots across connected facilities

## 🛠️ Technology Stack

- **Frontend**: HTML5, Tailwind CSS
- **Backend**: Django (Python)
- **Database**: SQLite3
- **Framework**: Django Web Framework

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/synapse.git
   cd synapse
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install Django and dependencies**
   ```bash
   pip install django
   pip install -r requirements.txt  # if you have a requirements file
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your web browser and navigate to `http://127.0.0.1:8000/`

## 💻 Usage

1. **For Patients**:
   - Browse available hospitals and laboratories in your area
   - View available appointment slots
   - Book appointments across different facilities
   - Manage your bookings from a single dashboard

2. **For Healthcare Providers**:
   - Register your facility on the platform
   - Manage appointment schedules
   - View and confirm patient bookings
   - Update facility information and services
