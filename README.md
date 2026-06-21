# Campus Placement Management System

A backend application built using FastAPI and PostgreSQL to manage campus placement activities.

## Features

* Student Registration
* Student Login with JWT Authentication
* Company Drive Creation
* Placement Application Tracking
* REST API Architecture
* PostgreSQL Database Integration
* SQLAlchemy ORM

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Uvicorn

## Project Structure

campus-placement-system/

├── app/

│ ├── main.py

│ ├── database.py

│ ├── models.py

│ ├── schemas.py

│ ├── auth.py

│ └── routes.py

├── requirements.txt

├── README.md

└── .gitignore

## Database Tables

### Students

* id
* name
* email
* password

### Companies

* id
* company_name
* role
* deadline
* oa_date

### Applications

* id
* student_id
* company_id
* status

## API Endpoints

### Authentication

POST /register

POST /login

### Companies

POST /companies

GET /companies

### Applications

POST /apply

GET /applications

## Future Enhancements

* Email Notifications
* OA Reminder System
* Interview Scheduling
* Admin Dashboard
* Role-Based Access Control
* Deployment on Render

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload

Open Swagger Documentation:

http://127.0.0.1:8000/docs
