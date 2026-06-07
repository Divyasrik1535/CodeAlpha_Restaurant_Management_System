# 🍽️ Restaurant Management System (Django REST API)

## 📌 Project Overview

This project is a **Restaurant Management System Backend** built using **Django** and **Django REST Framework**.

It is designed to handle real-world restaurant operations such as:

* Managing menu items
* Handling customer orders
* Table management
* Reservations
* Inventory updates
* Sales tracking

---

## 🎯 Key Features

### 🧾 Orders Management

* Create and manage orders
* Automatically calculates total amount
* Updates table status (available → occupied)

### 🍔 Menu Management

* Add and view menu items
* Each item includes price and available stock

### 🪑 Table Management

* Manage restaurant tables
* Track availability status

### 📅 Reservation System

* Book tables for specific date and time
* Prevents double booking of same table

### 📦 Inventory Management

* Automatically reduces stock when order is placed
* Restores stock when order is cancelled

### 💰 Daily Sales API

* Provides total orders and revenue for the day

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)

---

## 🔗 API Endpoints

### Menu

* `GET /api/menu/` → View all menu items

### Orders

* `GET /api/orders/` → View orders
* `POST /api/orders/` → Create order
* `GET /api/orders/daily_sales/` → View daily sales

### Tables

* `GET /api/tables/` → View tables

### Reservations

* `GET /api/reservations/` → View reservations
* `POST /api/reservations/` → Book table

---

## 🧠 Business Logic Implemented

* Prevents double booking of tables
* Auto-calculates order total
* Auto-updates inventory
* Handles order cancellation and stock restore

---

## 🚀 How to Run the Project

```bash
# Clone repository
git clone <your-repo-link>

# Navigate to project
cd restaurant_system

# Run server
python manage.py runserver
```

---

## 📊 Future Improvements

* Payment integration
* User authentication system
* Advanced reporting dashboard
* Notifications for reservations

## 🙌 Conclusion

This project demonstrates backend development skills including:

* API design
* Database relationships
* Real-world business logic implementation