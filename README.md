# smsm
Step 5: Version Control Report (Git/GitHub)
Student Management System Project
________________________________________
1. Introduction
This report documents the version control process used in Step 5 of the Student Management System project. Git was used as the local version control system, and GitHub served as the cloud-based remote repository. The project includes more than ten meaningful commits, each contributing non-trivial development progress such as implementing CRUD operations, creating views and templates, integrating authentication, and adding data visualization.
All commits follow descriptive and clear commit messages to ensure project traceability, maintainability, and transparency. The GitHub repository is publicly accessible and contains the full development history of the project.
________________________________________
2. GitHub Repository Link
Public Repository:
(Replace this with your actual link)
https://github.com/your-username/sms-project
________________________________________
3. Full Commit List (10+ Non-Trivial Commits)
Below is the list of all meaningful commits made during the development:
1.	Initialize Django project structure and create core app
2.	Add models: Student, Course, Instructor, Department, Enrollment
3.	Generate initial migrations and apply SQLite database schema
4.	Register all models in Django admin for database management
5.	Implement CRUD views and templates for Student management
6.	Add URL patterns for home page, authentication, and CRUD operations
7.	Integrate Django authentication system with login/logout templates
8.	Create database population script to insert sample records
9.	Add enrollment data visualization using Chart.js
10.	Add Bootstrap UI enhancements and CSS styling for dashboard
(If you made extra commits, include them here.)
________________________________________
4. Screenshots of Commit List
(Insert your screenshot here)
Add a screenshot from your GitHub repository showing the entire list of commits.
This verifies that your project contains at least 10 meaningful commits.
________________________________________
5. Screenshots of Three Major Commits
You must include screenshots highlighting three key commits. A recommended selection:
Commit 1: Add models and database schema
•	Introduced all five tables (Student, Instructor, Department, Course, Enrollment)
•	Created Django ORM structure
•	Generated initial migrations
(Insert screenshot here)
________________________________________
Commit 2: Implement Student CRUD operations
•	Added ListView, CreateView, UpdateView, DeleteView
•	Created corresponding templates
•	Registered routes in URLs
(Insert screenshot here)
________________________________________
Commit 3: Add Enrollment Chart Visualization
•	Added JSON endpoint for chart data
•	Integrated Chart.js on the frontend
•	Displayed student count per course graphically
(Insert screenshot here)
________________________________________
6. Summary
This step demonstrates the use of Git and GitHub as essential tools for software development. Version control ensured clean documentation of changes, traceability, collaborative readiness, and proper project management. All required conditions for Step 5 were fully met:
•	✔ Public GitHub repository
•	✔ Minimum 10 meaningful commits
•	✔ Screenshots of commit list
•	✔ Screenshots of three major commits
•	✔ Clear and structured commit messages






















📘 Student Management System (SMS)
A Django-based web application for managing student records, courses, instructors, departments, and enrollments with CRUD operations, authentication, data visualization, and SQLite integration.
________________________________________
🚀 Project Overview
The Student Management System is a full-stack Django application designed to manage and organize academic data efficiently. It includes key functionalities such as:
•	✔ User Authentication (Login/Logout)
•	✔ CRUD Operations for Students
•	✔ Relational Database with 5 Tables
•	✔ Data Visualization using Chart.js
•	✔ SQLite Database with Sample Data
•	✔ Git/GitHub Version Control
This project was completed as part of an academic assignment demonstrating relational databases, Django web development, and version control practices.
________________________________________
🏗️ Tech Stack
Frontend
•	HTML5
•	CSS3
•	Bootstrap 5
•	Chart.js
Backend
•	Python (Django Framework)
•	SQLite Database
•	Django ORM
Tools & Deployment
•	Git & GitHub
•	DB Browser for SQLite
•	Django Development Server
________________________________________
🗂️ Database Design
The system uses 5 relational tables:
1.	Student
2.	Course
3.	Instructor
4.	Department
5.	Enrollment
An ER diagram describes the relationships:
•	Students enroll in multiple courses (M:N via Enrollment)
•	Courses are taught by Instructors
•	Instructors belong to Departments
________________________________________
📊 Features
🔐 User Authentication
•	Secure login/logout system using Django's built-in authentication.
🧑🎓 Student Management (CRUD)
•	Create
•	Read
•	Update
•	Delete
📈 Data Visualization
•	Enrollment per course displayed using Chart.js bar chart.
🗃️ Sample Data
Database is preloaded using populate_db.py with:
•	10 Students
•	10 Instructors
•	10 Departments
•	10 Courses
•	20 Enrollment records
________________________________________
📦 Installation Guide
1. Clone the Repository
git clone https://github.com/your-username/sms-project.git
cd sms-project
2. Create Virtual Environment
python -m venv venv
Activate it:
Windows PowerShell:
venv\Scripts\Activate.ps1
Mac/Linux:
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py migrate
5. Populate Database (Optional)
python populate_db.py
6. Create Superuser
python manage.py createsuperuser
7. Run Server
python manage.py runserver


