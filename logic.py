from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def gen_page():
    return render_template("gen_page")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("hello.html", name=name)