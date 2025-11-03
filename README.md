# 🇳🇬 Citizens REST API (Django + DRF)

A simple Django REST API for managing citizen records.

---

## ⚙️ Setup

```bash
# 1. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows)

# 2. Install dependencies
pip install django djangorestframework

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start server
python manage.py runserver

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/citizens/`      | Create new citizen |
| GET    | `/api/citizens/`      | View all citizens  |
| GET    | `/api/citizens/{id}/` | View one citizen   |
| PUT    | `/api/citizens/{id}/` | Update all fields  |
| PATCH  | `/api/citizens/{id}/` | Update one field   |
| DELETE | `/api/citizens/{id}/` | Delete citizen     |

🧪 Test with Postman

GET → http://127.0.0.1:8000/api/citizens/

POST → http://127.0.0.1:8000/api/citizens/

GET → http://127.0.0.1:8000/api/citizens/1/

PUT/PATCH → http://127.0.0.1:8000/api/citizens/1/

DELETE → http://127.0.0.1:8000/api/citizens/1/

Author: Joy Ezenwoke ❤️
Built with Django REST Framework
