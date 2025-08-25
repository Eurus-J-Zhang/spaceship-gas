from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(1))
    age = db.Column(db.Integer)

    tank_practice = db.Column(db.String(10))
    
    history = db.Column(db.String(255), nullable=False)

    competence = db.Column(db.Integer)
    joy = db.Column(db.Integer)
    irritation = db.Column(db.Integer)
    boredom = db.Column(db.Integer)

    feedback = db.Column(db.String(600))

    agent = db.Column(db.String(10))
    power = db.Column(db.String(10))
    

    # so the names here will be in the database