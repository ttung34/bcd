from flask import Flask
from models import * #import file models.py previously created

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:trinhthanhtung30@localhost:5432/ORM"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #tie db with flask app


def main():
    flight = Flights(origin="HN1", destination="HCM", duration=540)
    db.session.add(flight)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context(): #allow developer interact with via command line
        main()