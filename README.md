Markdown# 🛒 Online Shopping API

A RESTful online shopping backend built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The application provides APIs for user authentication, role-based authorization, categories, products, shopping carts, and orders.

The project follows a layered architecture using routers, services, repositories, models, and schemas.

---

## 📌 Project Features

### Authentication and Users

- User registration
- User login using JWT authentication
- Password hashing with bcrypt
- Email validation
- Duplicate email checking
- Current-user endpoint
- Role-based authorization
- Customer and admin roles

### Categories

- Admin-only category creation
- View all categories
- Role-based access control

### Products

- Admin-only product creation
- View all products
- View product by ID
- Search products
- Product stock validation

### Shopping Cart

- Add a product to the cart
- View the authenticated user's cart
- Update cart quantity
- Remove an item from the cart
- Stock availability validation
- User-specific cart access

### Orders

- Checkout using cart items
- Calculate total order amount
- Create order details
- Clear the cart after checkout
- View order history
- View individual order details
- Prevent users from accessing other users' orders

### Application Quality

- Layered architecture
- JWT authentication
- Role-based authorization
- PostgreSQL database integration
- Request logging
- `app.log` file generation
- Background task processing
- HTTP exception handling
- Unit testing with pytest
- PostgreSQL integration testing
- Coverage validation

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Pydantic
- Python-JOSE
- Passlib
- Bcrypt
- Pytest
- Pytest-Cov
- Swagger UI

---

## 📂 Project Structure

```text
WEEK2-SHIVANI_KARUMURI/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── logging_config.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cart.py
│   │   ├── category.py
│   │   ├── order.py
│   │   ├── product.py
│   │   └── user.py
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── order_tasks.py
│   │
│   ├── database.py
│   └── main.py
│
├── repositories/
│   ├── cart_repository.py
│   ├── category_repository.py
│   ├── order_repository.py
│   ├── product_repository.py
│   └── user_repository.py
│
├── routers/
│   ├── auth_router.py
│   ├── cart_router.py
│   ├── category_router.py
│   ├── order_router.py
│   ├── product_router.py
│   └── user_router.py
│
├── schemas/
│   ├── cart_schema.py
│   ├── category_schema.py
│   ├── order_schema.py
│   ├── product_schema.py
│   └── user_schema.py
│
├── services/
│   ├── cart_service.py
│   ├── category_service.py
│   ├── order_service.py
│   ├── product_service.py
│   └── user_service.py
│
├── test/
│   ├── conftest.py
│   ├── test_security.py
│   ├── test_cart_service.py
│   ├── test_order_service.py
│   └── test_database_integration.py
│
├── .gitignore
├── app.log
├── pytest.ini
├── README.md
└── requirements.txt


🏗️ Application Architecture
The application follows a layered architecture:
Plain textClient
  ↓
Router
  ↓
Service
  ↓
Repository
  ↓
SQLAlchemy Model
  ↓
PostgreSQL Database

Routers
Routers define the API endpoints and handle HTTP requests.
Services
Services contain business logic, validation, authentication checks, and application rules.
Repositories
Repositories perform database operations using SQLAlchemy.
Models
Models represent the PostgreSQL database tables.
Schemas
Schemas validate incoming request data and format outgoing response data using Pydantic.

🗄️ Database Tables
The application uses the following tables:

users
categories
products
Cart
orders
order_details

The main relationships include:

A user can have multiple cart items.
A user can place multiple orders.
A product can belong to a category.
An order can contain multiple order details.
Cart items and order details reference products.


🔐 Authentication
The application uses JWT Bearer authentication.
Login Endpoint
Plain textPOST /api/auth/login

The login endpoint returns an access token.
In Swagger:

Open /api/auth/login.
Enter the email and password.
Execute the request.
Copy the returned access token.
Click Authorize.
Enter the token when prompted.

Swagger automatically sends the token to protected endpoints after authorization.
Protected Endpoint Example
Plain textGET /users/me

Expected response:
Plain text200 OK

Without a valid token, protected endpoints return:
Plain text401 Unauthorized


👥 User Roles
The application supports role-based authorization.
Customer
Customers can:

View products
View categories
Manage their cart
Checkout
View their orders

Admin
Admins can:

Create categories
Create products
Perform customer operations

Admin-only endpoints reject customer requests with:
Plain text403 Forbidden


📌 API Endpoints
Authentication and User APIs



Method
Endpoint
Description
Access




POST
/users/register
Register a new user
Public


POST
/api/auth/login
Login and receive JWT token
Public


GET
/users/me
Get the authenticated user's details
Authenticated




Category APIs



Method
Endpoint
Description
Access




POST
/categories/
Create a category
Admin


GET
/categories/
Get all categories
Public




Product APIs



Method
Endpoint
Description
Access




POST
/products/
Create a product
Admin


GET
/products/
Get all products
Public


GET
/products/{product_id}
Get a product by ID
Public


GET
/products/search/
Search products by name
Public



Example search request:
Plain textGET /products/search/?product_name=phone


Cart APIs



Method
Endpoint
Description
Access




POST
/cart/add
Add a product to the cart
Authenticated


GET
/cart/me
View the current user's cart
Authenticated


PUT
/cart/update/{cart_item_id}
Update cart quantity
Authenticated


DELETE
/cart/remove/{cart_item_id}
Remove an item from the cart
Authenticated



The cart is identified using the authenticated user's JWT. A user_id does not need to be supplied in the URL.

Order APIs



Method
Endpoint
Description
Access




POST
/orders/checkout
Place an order from the cart
Authenticated


GET
/orders/me
View the current user's order history
Authenticated


GET
/orders/{order_id}
View order details
Authenticated



Users can view only their own orders.

⚙️ Installation
1. Clone the Repository
Bashgit clone <repository-url>

2. Navigate to the Project
Bashcd week2-Shivani_Karumuri

3. Create a Virtual Environment
Bashpython -m venv env

4. Activate the Virtual Environment
Windows PowerShell
Unknown.\env\Scripts\Activate.ps1

Windows Command Prompt
Unknownenv\Scripts\activate

5. Install Dependencies
Bashpip install -r requirements.txt


🗄️ PostgreSQL Configuration
Create a PostgreSQL database, for example:
Plain textshopping_db

Configure the database connection in the application's database configuration.
Example:
PythonDATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/shopping_db"

Do not commit real database passwords or secret keys to Git.

▶️ Running the Application
Start the FastAPI server from the project root:
Bashuvicorn app.main:app --reload

The API will be available at:
Plain text http://127.0.0.1:8000


📖 API Documentation
Swagger UI:
Plain text http://127.0.0.1:8000/docs

OpenAPI JSON:
Plain text http://127.0.0.1:8000/openapi.json

ReDoc:
Plain text http://127.0.0.1:8000/redoc


📝 Logging
The application records request information in:
Plain textapp.log

The log includes:

HTTP method
Request path
Response status code
Request processing time
Successful requests
Failed requests
Invalid routes
Background task activity

Example log entry:
Plain text2026-08-13 15:56:15,666 | INFO | shopping_api |
POST /api/auth/login -> 200 in 0.787 seconds


⚙️ Background Processing
Background tasks are used for operations that do not need to delay the HTTP response, such as order-related processing and logging activities.
Background task functions are located in:
Plain textapp/tasks/order_tasks.py


🧪 Testing
The project uses pytest for unit testing and database integration testing.
Run all tests
Bashpython -m pytest -q

Run a specific test file
Bashpython -m pytest -q test/test_security.py

Run the PostgreSQL integration test without coverage
Bashpython -m pytest -q test/test_database_integration.py --no-cov

Run tests with coverage
Bashpython -m pytest --cov=app --cov=services --cov=repositories --cov-report=term-missing

Generate an HTML coverage report
Bashpython -m pytest --cov=app --cov=services --cov=repositories --cov-report=html

The HTML report is generated in:
Plain texthtmlcov/index.html

Open this file in a browser to view detailed coverage information.
Test Result
The completed test suite includes:

Security unit tests
Cart service unit tests
Order service unit tests
PostgreSQL database integration testing

Current validation result:
Plain text 9 passed
1 skipped
Coverage: 40%

The PostgreSQL integration test was also successfully executed separately against the dedicated test database.

🧰 Test Database
Integration tests should use a separate PostgreSQL database instead of the main application database.
Example test database:
Plain textshopping_api_test

Set the test database URL in PowerShell:
Unknown$env:TEST_DATABASE_URL="postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/shopping_api_test"

Run the integration test:
Unknownpython -m pytest -q test/test_database_integration.py --no-cov

The test inserts a temporary user into the test database and verifies that the record can be retrieved.

📊 Milestone Completion
Milestone 1: Authentication and Database

User registration completed
Password hashing completed
JWT login completed
Protected endpoints completed
PostgreSQL connection completed

Milestone 2: Role-Based Authorization

Customer role implemented
Admin role implemented
Admin-only category and product creation completed
Unauthorized role access returns 403 Forbidden

Milestone 3: Cart and Orders

Cart functionality completed
User-specific cart access completed
Checkout completed
Order history completed
Order details completed

Milestone 4
Skipped as instructed by the instructor.
Milestone 5: Async Processing and Application Quality

Background tasks implemented
Request logging implemented
app.log created
Exception handling implemented
Error responses validated

Milestone 6: Testing and Git Delivery

Unit tests implemented with pytest
PostgreSQL integration test implemented
Coverage validation configured
Minimum coverage requirement set to 40%
Git delivery prepared


🔒 Security Notes

Passwords are hashed before storage.
JWT tokens are used for authentication.
JWT secrets should be stored securely.
Database passwords should not be committed to Git.
The production JWT secret must be changed from the development default.
The test database should be separate from the application database.


📦 Git Delivery
Check the project status:
Bashgit status

Add the project files:
Bashgit add .

Create a commit:
Bashgit commit -m "Complete online shopping API and testing"

Push the project:
Bashgit push origin main

The following files should not be committed:
Plain textenv/
__pycache__/
.pytest_cache/
htmlcov/
.env
*.pyc


📚 Concepts Demonstrated

REST API development
FastAPI routing
Dependency injection
JWT authentication
Password hashing
Role-based authorization
CRUD operations
Layered architecture
SQLAlchemy ORM
PostgreSQL relationships
Pydantic validation
Background tasks
Application logging
Exception handling
Unit testing
Integration testing
Code coverage
Git version control


🚀 Future Enhancements

Alembic database migrations
Refresh tokens
Password reset functionality
Pagination for products and orders
Product image upload
Payment gateway integration
Email notifications
Redis caching
Docker deployment
CI/CD pipeline
Automated test execution through GitHub Actions
Admin dashboard


👩‍💻 Author
Shivani Karumuri

