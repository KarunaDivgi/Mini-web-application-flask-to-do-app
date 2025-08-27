Flask To-Do App
A simple web-based task management application built with Flask, allowing users to add, delete, and mark tasks as completed. Tasks are persistently stored using SQLite.

Features
Add Tasks: Easily add new tasks to your list.

Mark Complete: Toggle tasks as complete or incomplete.

Delete Tasks: Remove tasks from the list.

Persistent Storage: All tasks are saved to a SQLite database, so they are not lost when the application restarts.

Responsive UI: Styled with Bootstrap for a clean and mobile-friendly interface.

Technologies Used
Backend: Python 3, Flask

Database: SQLite (managed with Flask-SQLAlchemy)

Frontend: HTML, CSS (Bootstrap)

Deployment (Optional): Gunicorn (for production server)

Installation and Setup
Follow these steps to get the project up and running on your local machine.

Clone the Repository:

git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app

(If you haven't initialized a Git repository yet, you'll do this in Step 6 first, then you won't clone it to run locally, you'll just navigate to your existing folder.)

Create and Activate a Virtual Environment:
It's recommended to use a virtual environment to manage project dependencies.

On Windows:

python -m venv venv
.\venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install Dependencies:
With your virtual environment activated, install all required Python packages.

pip install -r requirements.txt

How to Run
Start the Flask Development Server:
Ensure your virtual environment is active and you are in the flask-todo-app directory.

python app.py

Access the Application:
Open your web browser and navigate to:
http://127.0.0.1:5000/

Usage
Add a Task: Type your task into the input field and click "Add Task".

Mark Complete/Incomplete: Click the "Mark Complete" or "Mark Incomplete" button next to a task.

Delete a Task: Click the "Delete" button next to a task.

Project Structure
flask_todo_app/
├── venv/                   # Python virtual environment
├── app.py                  # Main Flask application file
├── requirements.txt        # List of Python dependencies
├── Procfile                # Heroku/Render deployment configuration
├── README.md               # Project documentation
├── tasks.db                # SQLite database file (generated after first run)
└── templates/
    └── index.html          # HTML template for the user interface

Screenshots
(Replace these placeholders with actual screenshots of your application)


Initial empty To-Do list.


To-Do list with several tasks added.

