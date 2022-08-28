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
        print(myform.items)
        print(myform.get("editor"))
        
        if myform.get("editor") == "grid" or myform.get("editors_select") == "grid":
            print("using grid editor")
            return grid_input(myform)

        elif myform.get("editor") == "basic" or myform.get("editors_select") == "basic":
            print("using basic editor")

        else:
            pass



    return render_template("gen_page.html", context=mycontext)

def grid_input(form):

    mycontext = {}
    
    num_rows = form.get("num_rows")
    if num_rows:
        mycontext["num_rows"] = int(num_rows)
    else:
        mycontext["num_rows"] = 8

    return render_template("grid_input.html", context=mycontext)


@app.route("/hello", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        mydata = request.form["mytext"]
        print("hello " + mydata)
        return render_template("hello.html", context={"fill_text": mydata})
    return render_template("hello.html", context={"fill_text": ""})