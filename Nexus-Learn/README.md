
# 🎓 Nexus Learn



**Nexus Learn** is a modern, cloud-based academic workspace designed to streamline the student experience. It serves as a central "operating system" for students to manage timetables, finances, study materials, and extracurricular activities in a unified, high-performance interface.

Built with a **Glassmorphic** design language, it features smooth animations, a dark-themed UI, and seamless backend integration.

---

## ✨ Features

### 🖥️ **Command Center Dashboard**

* **At-a-Glance Overview:** Instant access to your next class, total monthly expenses, and recent cloud uploads.
* **Interactive Widgets:** Glassmorphic cards that provide quick summaries and navigation.
* **Personalized Greeting:** Dynamic welcome message and time-based context.

### 📚 **Academic Management**

* **Timetable Tracker:** visual schedule management for your classes.
* **Subject Organizer:** Manage courses, track difficulty levels, and store links to resources (YouTube/Wiki).
* **Notes Library:** Upload and organize study materials (PDFs, Docs) linked to specific subjects.

### 💰 **Student Finance**

* **Expense Tracker:** Log daily spending (Food, Transport, Stationery).
* **Budget Analytics:** View total expenditure at a glance to stay on budget.

### ☁️ **Nexus Cloud & Activities**

* **File Storage:** Securely upload and retrieve important project files and assignments.
* **Activity Logger:** Record extracurricular achievements, hackathons, and events.

### 🎨 **UI/UX Excellence**

* **Premium Glassmorphism:** Real-time backdrop blur, noise textures, and translucent layers.
* **Fluid Animations:** Powered by `motion-v` for spring-physics transitions and smooth entry effects.
* **Reactive Backgrounds:** Dynamic geometric shapes that breathe life into the application.

---

## 🛠️ Tech Stack

### **Frontend**

* **Framework:** [Vue.js 3](https://vuejs.org/) (Composition API)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/)
* **Animations:** [Motion One (motion-v)](https://motion.dev/)
* **Icons:** [Lucide Vue](https://lucide.dev/) & Radix Icons
* **State Management:** [Pinia](https://pinia.vuejs.org/)
* **HTTP Client:** Axios

### **Backend**

* **Framework:** Django / Django REST Framework
* **Database:** PostgreSQL 
* **Authentication:** JWT / Token-based auth

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### **Prerequisites**

* Node.js (v16.0.0 or higher)
* npm or yarn
* Python & Pip (for the backend)

### **1. Clone the Repository**

```bash
git clone https://github.com/Alwin42/Project_100/tree/main/Nexus-Learn
cd Nexus-Learn

```

### **2. Frontend Setup**

Navigate to the frontend directory and install dependencies.

```bash
cd frontend
npm install

```

**Run the development server:**

```bash
npm run dev

```

The app will be available at `http://localhost:5173`.

### **3. Backend Setup**

Navigate to the backend directory.

```bash
cd backend
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

```

The API will be available at `http://localhost:8000`.

---

## 📂 Project Structure

```bash
nexus-learn/
├── src/
│   ├── assets/            # Static assets (images, global CSS)
│   ├── components/        # Reusable UI components
│   │   ├── ui/            # Shadcn/Base UI components (Buttons, Inputs, Cards)
│   │   ├── Navbar.vue     # Global Navigation
│   │   └── BackgroundShapes.vue # Animated background
│   ├── services/          # API service configuration (Axios)
│   ├── stores/            # Pinia state stores (Auth, User data)
│   ├── views/             # Page views
│   │   ├── HomeView.vue   # Main Dashboard
│   │   ├── LoginView.vue  # Auth Pages
│   │   └── forms/         # Data Entry Forms (Add Subject, Expense, etc.)
│   └── App.vue            # Root Component
└── ...

```

---

