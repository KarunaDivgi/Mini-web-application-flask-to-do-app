from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# Database config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gmail'  # sender gmail
app.config['MAIL_PASSWORD'] = 'password' #password
app.config['MAIL_DEFAULT_SENDER'] = 'gmail'  # SAME AS USERNAME

mail = Mail(app)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Home/Dashboard
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'verified' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        task_desc = request.form.get('task_description')
        due_date = request.form.get('due_date')
        user_email = session.get('email')

        if task_desc and due_date:
            new_task = Task(description=task_desc, due_date=due_date)
            db.session.add(new_task)
            db.session.commit()

            # Send task added email
            try:
                msg = Message('📝 Task Added', recipients=[user_email])
                msg.body = f"You've successfully added a new task:\n\n{task_desc}\nDue: {due_date}"
                mail.send(msg)
            except Exception as e:
                print(f"[ERROR] Failed to send task email: {e}")

            flash("Task added successfully!", "success")
            return redirect(url_for('index'))

    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Mark task complete/incomplete
@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

# Delete task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Login (email + send OTP)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash("Email is required!", "danger")
            return render_template('login.html')

        otp = str(random.randint(1000, 9999))
        session['otp'] = otp
        session['email'] = email

        try:
            msg = Message("🔐 Your OTP Code", recipients=[email])
            msg.body = f"Your OTP for login is: {otp}"
            mail.send(msg)
            flash("OTP sent to your email!", "info")
        except Exception as e:
            print(f"[ERROR] Failed to send OTP email: {e}")
            flash("Failed to send OTP. Try again later.", "danger")

        return redirect(url_for('verify'))

    return render_template('login.html')

# Verify OTP
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form.get('otp')
        if user_otp == session.get('otp'):
            session['verified'] = True
            return render_template('verify.html', verified=True)
        else:
            flash("❌ Invalid OTP. Try again.", "danger")
    return render_template('verify.html', verified=False)

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You’ve been logged out.", "info")
    return redirect(url_for('login'))

# Run server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
