# 📝 fastapi-minimal-CRUD 
## Educational Task Manager API

A minimalist, containerized REST API built with **Python**, **FastAPI**, and **SQLAlchemy**. This project is designed for educational purposes to demonstrate the full lifecycle of HTTP methods, containerization, and ORM integration using SQLite.

---

## 🚀 Features
* **Modern Stack:** FastAPI (Python 3.12+) & SQLAlchemy 2.0.
* **Database:** SQLite (File-based, ephemeral for testing).
* **Documentation:** Automatic OpenAPI (Swagger) generation.
* **Containerized:** Multi-stage Docker build for a minimal footprint (~120MB).
* **CRUD Operations:** Implements GET, POST, PUT, and DELETE.

---

## 🛠 Prerequisites
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

---

## 📥 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/jhasensio/fastapi-minimal-crud.git
cd fastapi-minimal-crud
```

### 2. Launch with Docker Compose
This command builds the minimal image and starts the server.
```bash
docker-compose up --build -d
```

### 3. Access the API

This command builds the minimal image and starts the server.
- **API Root:** `http://localhost:8000/api/tasks`
- **Interactive Swagger Docs:** `http://localhost:8000/docs`
- **Alternative ReDoc:** `http://localhost:8000/redoc`


### API Endpoints
| Method      | Endpoint         |  Description                                    |  
| :---        | :----            | :---                                            |
| **GET**     | `/api/tasks`     | Retrieve all tasks from the database.           |
| **POST**    | `/api/tasks`     | Create a new task. (Do not include `task_id`).s |
| **PUT**     | `/api/tasks{id}` | Update/Replace an existing task by ID.          |
| **DELETE**  | `/api/tasks{id}` | Remove a task from the database.                |

### Example Request (Create Task)
```bash
curl -X 'POST' \
  'http://localhost:8000/api/tasks' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Learn Docker and FastAPI",
  "completed": false
}'
```

### 🏗 Project Structure
- `main.py` - Contains the API logic, SQLAlchemy models, and Pydantic schemas.
- `Dockerfile` - Multi-stage build using Alpine Linux for size optimization.
- `docker-compose.yml` - Orchestrates the container and persists the `test.db file.
- `test.db` - SQLite database file (generated automatically).

### 🐍 Running Locally (Native Python)

If you prefer not to use Docker, you can run the API directly on your machine using a Virtual Environment (`venv`).

### 1. Create and Activate a Virtual Environment
This keeps the project dependencies isolated from your system Python.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv\bin\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### Create the `requirements.txt`
```bash
fastapi[standard]
sqlalchemy
requests
```

### Launch the Server
Use `fastapi dev` for a development environment with auto-reload (restarts whenever you save `main.py`):
```bash
fastapi dev main.py
```
_The API will be available at: `http://127.0.0.1:8000/api/tasks`_


### Testing the installation 
```bash
# Run the automated test script
python test_api.py
```

