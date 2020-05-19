from flask import Flask, render_template, request, session
from flask_session import Session
import json

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
@app.route('/index/',  methods=["GET", "POST"])
def index():
    return render_template("index.html")



@app.route("/add_course/", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return render_template("add_course.html")



@app.route("/find_learners/", methods=["GET", "POST"])
def find_learners():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return render_template("find_learners.html")




@app.route("/search_course/", methods=["GET", "POST"])
def search_course():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return render_template("search_course.html")
