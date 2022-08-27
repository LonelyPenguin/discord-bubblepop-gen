import flask
from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def gen_page():
    return render_template("gen_page.html")

@app.route("/hello", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        mydata = request.form["mytext"]
        print("hello " + mydata)
        return render_template("hello.html", context={"fill_text": mydata})
    return render_template("hello.html")