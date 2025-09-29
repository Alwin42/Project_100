## EcoSync - Waste Management System

EcoSync is a web-based platform designed to streamline waste collection and management in Kochi. Built with Django, this project provides an intuitive interface for residents to schedule waste pickups and for collectors to manage their routes efficiently, promoting a cleaner and more sustainable urban environment.

---
## Features

- **User Authentication**: Secure registration and login system for residents and waste collectors.
- **Waste Pickup Requests**: Residents can easily schedule pickups for different categories of waste (e.g., organic, plastic, e-waste).
- **Request Management**: A dashboard for users to view the status of their pickup requests (Pending, Completed).
- **Admin Panel**: A comprehensive Django admin interface for managing users, requests, and reports.
- **Responsive Design**: A clean, mobile-first interface built with Tailwind CSS.

---
## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite3
- **Version Control**: Git

---
## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Eco-Sync.git](https://github.com/your-username/Eco-Sync.git)
    cd Eco-Sync
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For MacOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.