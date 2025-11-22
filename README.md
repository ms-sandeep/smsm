#Student Management System (CRUD Application)
🎓 Student Management System
A complete CRUD-based web application built using Django, SQLite, Bootstrap, and Chart.js.
This project demonstrates database design, user authentication, CRUD operations, data visualization, and version control with Git/GitHub.
________________________________________
🚀 Project Overview
The Student Management System (SMS) is a web-based application designed to manage student information for an educational institution.
It enables administrators to:
•	Create, Read, Update, and Delete student data
•	Manage instructors, courses, and departments
•	View enrollment statistics with charts
•	Authenticate users through Django’s secure login system
This application follows a modular structure and uses a relational database designed in 3rd Normal Form (3NF).
________________________________________
🛠️ Tech Stack
Component	Technology
Backend	Django (Python)
Database	SQLite
Frontend	HTML, CSS, Bootstrap
Charts	Chart.js
Version Control	Git & GitHub
Tools	DB Browser for SQLite
________________________________________
📂 Features
✔ 1. User Authentication
•	Secure login/logout using Django Auth
•	Protected views for CRUD operations
✔ 2. Full CRUD Operations
Manage the following entities:
•	Student
•	Course
•	Instructor
•	Department
•	Enrollment
Includes:
•	Add new record
•	Edit existing record
•	Delete record
•	Display all records
✔ 3. Data Visualization
Interactive Bar Chart showing:
•	Number of students enrolled in each course
•	Generated dynamically using Chart.js
•	Data served through Django JSON endpoints
✔ 4. Database Integration
•	SQLite relational DB
•	5 tables, each with 10+ rows
•	Data populated using custom script (populate_db.py)
________________________________________
📦 Project Structure
sms_project/
│
├── core/
│   ├── migrations/
│   ├── templates/core/
│   ├── static/core/css/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── sms_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── populate_db.py
├── manage.py
└── README.md
________________________________________
🗄️ Database Models
Student
Field	Type
name	CharField
dob	DateField
email	EmailField
address	TextField
Course
•	course_name
•	credits
•	instructor (FK)
Instructor
•	name
•	email
•	department (FK)
Department
•	dept_name
•	location
Enrollment
•	student (FK)
•	course (FK)
•	grade
•	semester
•	year
________________________________________
🔧 How to Run the Project
1. Clone the Repository
git clone https://github.com/Swetha-kasturi1919/sms-project.git
cd sms-project
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py migrate
5. Populate Sample Data (Optional)
python populate_db.py
6. Run Development Server
python manage.py runserver
Open in browser:
👉 http://127.0.0.1:8000/
________________________________________
📈 Data Visualization Overview
The dashboard includes:
•	Enrollment count per course
•	Dynamic chart created using Chart.js
•	Data retrieved through a Django JSON API endpoint
________________________________________
🧪 Sample Admin User
Username: admin
Password: admin
________________________________________
💾 GitHub Version Control
This project contains:
•	10+ meaningful commits
•	Clear and descriptive commit messages
•	Major commits include:
o	Model creation
o	CRUD operations
o	Authentication system
o	Chart visualization
o	Database population script

