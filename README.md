# fastapi-notes
FastApi  notes
# 📝 FastAPI Notes Backend

This is a simple and efficient notes management API built using [FastAPI](https://fastapi.tiangolo.com/). It supports full CRUD operations for managing notes.

## 🚀 Features

- Create, Read, Update, and Delete notes
- Fast and modern Python web framework (FastAPI)
- Interactive API docs with Swagger and ReDoc
- Environment-based configuration
- JWT authentication
-  PostgreSQL support

---

## 📁 Project Structure

```
fastapi-notes/
├── app/
│   ├── main.py            # Entry point (run with uvicorn)
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # DB operations
│   ├── database.py        # DB connection setup
│   └── routes.py          # API route definitions
├── .env                   # Environment variables
├── requirements.txt       # Project dependencies
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bisher-muhammed/fastapi-notes.git
cd fastapi-notes
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and define:



### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The server will be running at:  
**http://127.0.0.1:8000**

---

## 📚 API Documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Requirements

- Python 3.8+
- Uvicorn
- FastAPI
- SQLAlchemy
- Pydantic
- python-dotenv

All required packages are listed in `requirements.txt`.

---






---

## 🧑‍💻 Author

**Mohammed Bishar**  
GitHub: [@bisher-muhammed](https://github.com/bisher-muhammed)

---



