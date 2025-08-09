
## 🚀 MongoDB with Django Major Project

## Demo Video 

https://youtu.be/BFjCalYXTrk?si=RYYId9tKVVPyuYA1

## 📜Project Description
This is a full-stack web application built using the Django framework that demonstrates the seamless integration with a MongoDB database. The project allows users to add and view person data, showcasing a practical implementation of Django's ORM with a NoSQL database.

## ✨Features
## Data Insertion: 
Create and save new person records (FirstName, LastName, Age, Location) to a MongoDB database via a simple web form.

## Data Retrieval:
Fetch and display all stored person data from the database on a dedicated template page.

## Django Migrations:
Utilizes Django's built-in migration system to manage the database schema in MongoDB.

## 🛠️ Tech Stack
Backend Framework: Python (Django)

Database: MongoDB

Database Connector: Djongo

Frontend: HTML, CSS

# ⚙️ Getting Started
Prerequisites
Python 3.x

pip (Python package installer)

A running instance of MongoDB (usually on mongodb://localhost:27017/)
# Installation
## Clone the repository:
git clone https://github.com/harshitha-shetty11/Mongo_Django_Major_Project.git

cd Mongo_Django_Major_Project
## Create and activate a virtual environment:
python -m venv venv
## On Windows:
venv\Scripts\activate
## On macOS/Linux:
source venv/bin/activate
Configure the database settings in mongo_django_project/settings.py to match your MongoDB setup.
## Run database migrations:
python manage.py makemigrations data_app

python manage.py migrate
## Start the development server:
python manage.py runserver
# 🖥️ Usage
Open your browser and navigate to http://127.0.0.1:8000/people/add/ to add new person data.

Visit http://127.0.0.1:8000/people/list/ to view all the data stored in the MongoDB database.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
