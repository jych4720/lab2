from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_year = request.form.get('bornyear')
    return render_template("hello.html", name=input_name,
                           age=input_age, bornyear=input_year)


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif query == "asteroids":
        return "Unknown"
    elif query == "What is your name?":
        return "jc4720"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get('q')
    if query_param:
        result = process_query(query_param)
    else:
        result = "Query parameter 'q' is missing."
    return result
