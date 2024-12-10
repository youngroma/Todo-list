# Todo List Application

A simple Django-based To-Do List application that allows users to:
- Add new tasks
- View a list of tasks
- Delete tasks

---

## Requirements

To run this project, make sure you have the following installed:
- Python 3.8 or higher
- Django 4.2 or higher
- SQLite (pre-installed with Python)

---

## Setup Instructions

Follow the steps below to set up the project locally:

### 1. **Clone the repository**

```bash
git clone https://github.com/youngroma/Todo-list.git
cd Todo-list
```

# 2. Set up a virtual environment
Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

# 3. Install project dependencies
```bash
pip install -r requirements.txt
```

# 4. Set up the database
```bash
python manage.py migrate
```

# 5.  Run the development server
```bash
python manage.py runserver
```



