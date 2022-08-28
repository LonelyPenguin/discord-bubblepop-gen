import flask
from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def gen_page():
    
    mycontext = {}

    if request.method == "POST":

        myform = request.form

        if myform.get("editor") == "grid" or myform.get("editors_select") == "grid":
            print("using grid editor")
            return grid_input(myform)

        elif myform.get("editor") == "basic" or myform.get("editors_select") == "basic":
            print("using basic editor")

    return render_template("gen_page.html", context=mycontext)

def grid_input(form):

    mycontext = {}

    # get inputted dimensions, if any
    num_rows = form.get("num_rows")
    num_cols = form.get("num_cols")
    autofill = form.get("autofill")

    # set defaults, to be overriden
    mycontext["set_rows"] = 8
    mycontext["set_cols"] = 8
    mycontext["prefill"] = ""

    # override defaults, if dimensions provided
    if num_rows:
        mycontext["set_rows"] = int(num_rows)
    if num_cols:
        mycontext["set_cols"] = int(num_cols)
    if autofill:
        mycontext["prefill"] = autofill

    return render_template("grid_input.html", context=mycontext)


@app.route("/hello", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        mydata = request.form["mytext"]
        print("hello " + mydata)
        return render_template("hello.html", context={"fill_text": mydata})
    return render_template("hello.html", context={"fill_text": ""})