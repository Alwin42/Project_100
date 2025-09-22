# Deadline-Dash

A simple and intuitive web application that helps students track their exam deadlines by calculating the number of days remaining until each exam date.

## Features

- **Easy Date Entry**: Simple interface to add exam dates and subjects
- **Countdown Calculator**: Automatically calculates days remaining until each exam
- **Clean UI**: Modern, responsive design built with Tailwind CSS
- **Persistent Storage**: Exam data is stored in SQLite database
- **Real-time Updates**: Days remaining are calculated dynamically

## Tech Stack

- **Frontend**: HTML5, Tailwind CSS
- **Backend**: Python Flask
- **Database**: SQLite3
- **Templating**: Jinja2 (Flask's default)

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Alwin42/Project_100.git
   cd Deadline-Dash
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Add exam deadlines**:
   - Enter the exam subject/name
   - Select the exam date
   - Click "Add Exam" to save

4. **View countdown**: The application will automatically display how many days are left for each exam
