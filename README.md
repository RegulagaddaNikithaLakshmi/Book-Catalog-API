#  Book Catalog API

## Project Overview

Book Catalog API is a RESTful backend service built with Django & DRF for managing books efficiently. 

## ✨ Key Features
🆕 Create new books  
📖 Retrieve all or specific books  
✏️ Update existing books  
❌ Delete books  
⚡ Lightweight, scalable, and ready for production  

## 🛠️ Technology Stack

🐍 Python 3.x  
🌐 Django 5.x  
🔧 Django REST Framework 3.x  
💾 SQLite (or PostgreSQL/MySQL)  
🚀 Gunicorn (for production)

## 🚀 Installation & Setup

1. Clone the repository  

git clone https://github.com/RegulagaddaNikithaLakshmi/Book-Catalog-API.git

cd Book-Catalog-API

Create a virtual environment


python -m venv venv

**# Windows**

venv\Scripts\activate

**# Linux/Mac**

source venv/bin/activate

Install dependencies:


pip install -r requirements.txt

Apply database migrations



python manage.py migrate


Run the development server:

python manage.py runserver

**📄 API Endpoints:**

Method	Endpoint	Description

GET	/api/books/	Retrieve all books

POST	/api/books/	Create a new book

GET	/api/books/{id}/	Retrieve a specific book

PUT	/api/books/{id}/	Update a book

DELETE	/api/books/{id}/	Delete a book





**📄 License:**

   MIT License

