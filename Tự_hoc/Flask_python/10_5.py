from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.comfig["SQLALCHEMY_DATABASE_URI"]="postgesql://postgers:thanhtung3434342004@localhost:5432/flight"
app.comfig["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db.init_app(app)

def main():
    flights= FLight.query.filter_by(origin="Ha Noi").all()
    for flight in flights:
        pritn(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")
        
if __name__ == "__main__":
    with app.app_context():
        main()