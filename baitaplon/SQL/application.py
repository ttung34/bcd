from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://posgres:trinhthanhtung30@127.0.0.2:5432/ORM")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    diemsv = db.execute("SELECT * FROM diemsv").fetchall()
    return render_template("index.html", diemsv=diemsv)

@app.route("/tracuu", methods=["POST"])
def tracuu():
    """Tra cuu diem"""
    tensv = request.form.get("tensv")
    diemsv_id = int(request.from.get("diemsv_id"))

    db.execute("INSERT INTO python (tensv, diemsv_id) VALUES (: tensv, :diemsv_id)", 
               {"tensv":tensv, "diemsv_id": diemsv_id})
    db.commit()
    return render_template("success.html")
