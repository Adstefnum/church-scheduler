from flask import Flask, render_template, request
from models import db  # Import the db object from models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/users.db'  # Path to the database file
db.init_app(app)

from flask import render_template
from models import db, User, SundaySchedule, TuesdaySchedule, FridaySchedule
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sunday', methods=['GET', 'POST'])
def sunday():
    if request.method == 'POST':
        # Handle form submission and update the Sunday schedule
        # Retrieve user IDs from the form and update the corresponding SundaySchedule entries
        # You may want to perform additional validation and error handling here
        return 'Sunday schedule updated successfully!'
    else:
        users = User.query.all()
        sunday_schedule = SundaySchedule.query.first()
        return render_template('sunday.html', users=users, schedule=sunday_schedule)

@app.route('/tuesday', methods=['GET', 'POST'])
def tuesday():
    if request.method == 'POST':
        # Handle form submission and update the Tuesday schedule
        # Retrieve user IDs from the form and update the corresponding TuesdaySchedule entries
        # You may want to perform additional validation and error handling here
        return 'Tuesday schedule updated successfully!'
    else:
        users = User.query.all()
        tuesday_schedule = TuesdaySchedule.query.first()
        return render_template('tuesday.html', users=users, schedule=tuesday_schedule)

@app.route('/friday', methods=['GET', 'POST'])
def friday():
    if request.method == 'POST':
        # Handle form submission and update the Friday schedule
        # Retrieve user IDs from the form and update the corresponding FridaySchedule entries
        # You may want to perform additional validation and error handling here
        return 'Friday schedule updated successfully!'
    else:
        users = User.query.all()
        friday_schedule = FridaySchedule.query.first()
        return render_template('friday.html', users=users, schedule=friday_schedule)
