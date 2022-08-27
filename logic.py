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
        print(myform)
        mycontext["num_rows"] = int(myform["num_rows"])

    else:
        mycontext["num_rows"] = 8

    return render_template("gen_page.html", context=mycontext)




@app.route("/hello", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        mydata = request.form["mytext"]
        print("hello " + mydata)
        return render_template("hello.html", context={"fill_text": mydata})
    return render_template("hello.html")