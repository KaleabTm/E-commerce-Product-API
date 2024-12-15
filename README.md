E-Commerce Product and Order Management API
Description
This project implements an API for managing products, categories, shopping carts, and orders in an e-commerce platform. The API supports product CRUD operations, category management, cart management, order creation, and user authentication.

Features
Product Management: Add, update, delete, and view product details.
Category Management: Manage product categories.
Cart Management: Add, view, update, and delete cart items.
Order Management: Place orders and track order statuses.
Endpoints Implemented
1. Product Creation Endpoint
URL: /api/products/create/
Method: POST
Description: Adds a new product to the database.

Request Example:
json
Copy code
{
    "name": "Laptop",
    "description": "A high-performance laptop",
    "price": 1200.00,
    "stock": 5,
    "category": "Electronics",
    "created_by": "user@example.com"
}
Response Example:
json
Copy code
{
    "name": "Laptop",
    "description": "A high-performance laptop",
    "price": 1200.00,
    "stock": 5,
    "category": "Electronics",
    "created_by": "user@example.com"
}
2. Product Listing Endpoint
URL: /api/products/
Method: GET
Description: Retrieves a list of all products in the database.

Response Example:
json
Copy code
[
    {
        "name": "Laptop",
        "description": "A high-performance laptop",
        "price": 1200.00,
        "stock": 5,
        "category": "Electronics",
        "created_by": "user@example.com"
    },
    {
        "name": "Phone",
        "description": "A smartphone",
        "price": 700.00,
        "stock": 10,
        "category": "Electronics",
        "created_by": "admin@example.com"
    }
]
Setup Instructions
Prerequisites
Python 3.10 or higher
Django 5.1
PostgreSQL
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
Configure the .env file with database and other settings:

Create a .env file in the root of your project.
Add the following configuration to .env:
makefile
Copy code
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
Run database migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver


Additional Information
This project uses Django REST framework for building the API.
PostgreSQL is used as the database.
You can extend the API with more features like cart management, order management, and authentication.