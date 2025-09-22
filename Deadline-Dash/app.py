from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/exams')
def show_exams():
    
    exam_data = [
        {
            "name": "Quantum Physics Final",
            "date_obj": datetime.date(2025, 10, 15)
        },
        {
            "name": "Organic Chemistry Mid-term",
            "date_obj": datetime.date(2025, 11, 2)
        },
        {
            "name": "Data Structures Project",
            "date_obj": datetime.date(2025, 12, 10)
        }
    ]

    # Process the data to calculate days_left
    today = datetime.date.today()
    processed_exams = []
    for exam in exam_data:
        delta = exam["date_obj"] - today
        processed_exams.append({
            "name": exam["name"],
            "date": exam["date_obj"].strftime("%B %d, %Y"), # e.g., "October 15, 2025"
            "days_left": delta.days
        })

    # Pass the processed list to the template
    return render_template('exams.html', exams=processed_exams)

if __name__ == '__main__':
    app.run(debug=True)