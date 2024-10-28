from flask import Flask, render_template, request
import re


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
    match = re.match(r"What is (\d+) plus (\d+)\?", query)
    if match:
        # Extract the numbers and calculate the sum
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 + num2
        return str(result)
    match_largest = re.match(
        r"Which of the following numbers is the largest: ([\d, ]+)\?", query
    )
    if match_largest:
        numbers = list(map(int, match_largest.group(1).split(',')))
        largest_number = max(numbers)
        return str(largest_number)
    return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get('q')
    if query_param:
        result = process_query(query_param)
    else:
        result = "Query parameter 'q' is missing."
    return result
