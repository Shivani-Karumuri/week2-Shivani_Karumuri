# 🛒 Online Shopping Application (FastAPI + PostgreSQL)

## 📌 Project Overview

This project is a RESTful Online Shopping Application developed using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. It provides backend APIs for managing users, categories, products, shopping carts, and orders.

The application follows a layered architecture consisting of **Routers, Services, Repositories, Models, and Schemas**, making the project modular, scalable, and easy to maintain.

---

## 🚀 Features

### User Module
- User Registration
- User Login
- Email Validation
- Duplicate Email Check

### Category Module
- Create Category
- View All Categories

### Product Module
- Add Product
- View All Products
- View Product by ID
- Search Products

### Cart Module
- Add Product to Cart
- View Cart
- Update Cart Quantity
- Remove Product from Cart

### Order Module
- Checkout (Place Order)
- View Order History
- View Order Details

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn
- Swagger UI

---

## 📂 Project Structure

```text
shopping-api/
│
├── app/
│ ├── main.py
│ ├── database.py
│ │
│ ├── models/
│ │ user.py
│ │ category.py
│ │ product.py
│ │ cart.py
│ │ order.py
│ │
│ ├── schemas/
│ │ user_schema.py
│ │ category_schema.py
│ │ product_schema.py
│ │ cart_schema.py
│ │ order_schema.py
│ │
│ ├── repositories/
│ ├── services/
│ └── routers/
│
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Tables

- Users
- Categories
- Products
- Cart
- Orders
- Order Details

---

## 🏗️ Architecture

The project follows a layered architecture:

```
Client

↓

Router

↓

Service

↓

Repository

↓

Database
```

### Router
Handles incoming HTTP requests.

### Service
Contains business logic and validations.

### Repository
Performs database operations using SQLAlchemy.

### Models
Represent database tables.

### Schemas
Validate request and response data using Pydantic.

---

## 📌 API Endpoints

### User APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users/register` | Register User |
| POST | `/users/login` | User Login |

---

### Category APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/categories/` | Create Category |
| GET | `/categories/` | Get All Categories |

---

### Product APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/products/` | Add Product |
| GET | `/products/` | Get All Products |
| GET | `/products/{product_id}` | Get Product by ID |
| GET | `/products/search` | Search Products |

---

### Cart APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/cart/add` | Add Product to Cart |
| GET | `/cart/{user_id}` | View Cart |
| PUT | `/cart/update/{cart_item_id}` | Update Cart Quantity |
| DELETE | `/cart/remove/{cart_item_id}` | Remove Product from Cart |

---

### Order APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/orders/checkout` | Place Order |
| GET | `/orders/history/{user_id}` | View Order History |
| GET | `/orders/{order_id}` | View Order Details |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project

```bash
cd week2-Shivani_Karumuri
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Create a PostgreSQL database and update the connection string in `database.py`.

Example:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/shopping_db"
```

---

### Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After running the application, Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Testing

The APIs can be tested using:

- Swagger UI
- Postman

---

## 📚 Concepts Used

- REST API Development
- CRUD Operations
- Layered Architecture
- SQLAlchemy ORM
- Pydantic Validation
- Dependency Injection
- PostgreSQL Relationships
- Exception Handling

---

## 🎯 Future Enhancements

- JWT Authentication
- Password Hashing
- Order Detail Management
- Product Image Upload
- Payment Integration
- Admin Dashboard

---

## 👩‍💻 Author

**Shivani Karumuri**

