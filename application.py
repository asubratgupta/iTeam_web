from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     note = request.form.get("note")
    #     notes.append(note)

    return render_template("index.html")



@app.route("/add_course/", methods=["GET", "POST"])
def add_course():
    return render_template("add_course.html")



@app.route("/find_learners/", methods=["GET", "POST"])
def find_learners():
   return render_template("find_learners.html")




@app.route("/search_course/", methods=["GET", "POST"])
def search_course():
    return render_template("search_course.html")
