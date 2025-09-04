# 🚀 FastAPI User Management API

This project is a simple **User Management REST API** built with **FastAPI**, **SQLAlchemy**, and **Pydantic**.
It supports **CRUD operations** (Create, Read, Update, Delete) on users stored in a database.

---

## 📌 Features

- Add new users with validation (`username`, `email`)
- Get all users or filter by username
- Get user by ID
- Update user details (full or partial update)
- Delete user by ID
- Proper error handling with HTTP status codes

---

## 🛠️ Tech Stack

- **FastAPI** — high-performance Python web framework
- **SQLAlchemy ORM** — database interaction
- **SQLite** (default, can be swapped with PostgreSQL/MySQL)
- **Pydantic** — request/response validation

---

## 📂 Project Structure

```
.
├── __init__.py
├── __pycache__
│   ├── db.cpython-312.pyc
│   ├── main.cpython-312.pyc
│   └── models.cpython-312.pyc
├── db.py
├── main.py
├── models.py
├── Readme.md
├── requirements.txt
├── schemas.py
└── users.db

2 directories, 11 files
```
