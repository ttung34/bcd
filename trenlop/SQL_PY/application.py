from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:trinhthanhtung30@127.0.0.2:5432/ORM")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    name = request.form.get("name")
    flight_id = int(request.from.get.("flight_id"))

    db.execute("INSERT INTO passenger (name, flight_id) VALUE (:name, :flight_id)",
               {"name":name, "flight_id":flight_id})
    
    db.commit()
    return render_template("success.html")
