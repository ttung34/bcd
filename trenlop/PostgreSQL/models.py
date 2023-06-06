from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flights(db.Model):
    __tablename__ = "Flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nulable = False)
    destination = db.Column(db.String, nulable=False)
    duration = db.Column(db.Integer, nullable = False)
    
    
class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable =False)
    flight_id = db.Column(db.Integer,db.ForeignKey("flights.id"), nullable= False)
    
class User(db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique= True)
    password = db.Column(db.String(40), nullable= False)
    created = db.Column(db.DateTime, default = datetime.now)
    edited = db.Column(db.Datetime, onupdate = datetime.now)