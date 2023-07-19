from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    pastorate = db.Column(db.Boolean, default=False)
    ministered_last = db.Column(db.Date)

    def __repr__(self):
        return f"User(name='{self.name}', surname='{self.surname}', ministered_last='{self.get_ministered_last()}')"

    def get_ministered_last(self):
        if self.ministered_last:
            days_passed = (datetime.now().date() - self.ministered_last).days
            weeks_passed = days_passed // 7
            if weeks_passed == 1:
                return "1 week ago"
            else:
                return f"{weeks_passed} weeks ago"
        else:
            return "Never ministered"


class SundaySchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    call_to_worship = db.Column(db.Integer, db.ForeignKey('user.id'))
    beloved_revival_prayer_session = db.Column(db.Integer, db.ForeignKey('user.id'))
    praise_and_worship = db.Column(db.Integer, db.ForeignKey('user.id'))
    testimony = db.Column(db.Integer, db.ForeignKey('user.id'))
    prayer = db.Column(db.Integer, db.ForeignKey('user.id'))
    bible_reading = db.Column(db.Integer, db.ForeignKey('user.id'))
    special_ministration = db.Column(db.Integer, db.ForeignKey('user.id'))
    the_word = db.Column(db.Integer, db.ForeignKey('user.id'))
    offering_announcement_first_timers_welcome = db.Column(db.Integer, db.ForeignKey('user.id'))
    closing_prayers = db.Column(db.Integer, db.ForeignKey('user.id'))

class TuesdaySchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id'))

class FridaySchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    leader = db.Column(db.Integer, db.ForeignKey('user.id'))

