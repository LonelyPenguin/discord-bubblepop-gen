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
            #use grid editor
            return grid_input(myform)

        elif myform.get("editor") == "basic" or myform.get("editors_select") == "basic":
            # use basic editor

            try:
                input = myform.get("freeform_entry")
                in_rows = input.splitlines()

                #check input instead of each row to be consistent with splitting behaviour for whole input
                if "," in input:
                    rows_and_columns = [row.split(",") for row in in_rows]
                else:
                    rows_and_columns = [row.split(" ") for row in in_rows]

                spoilered_rows = []
                for row in rows_and_columns:
                    spoilered_rows.append("||" + "||||".join(row) + "||")

                output = "\n".join(spoilered_rows)

                mycontext["final_output"] = output

            except AttributeError:
                pass

    return render_template("gen_page.html", context=mycontext)

def grid_input(form):

    mycontext = {}

    # get inputted dimensions, if any
    num_rows = form.get("num_rows")
    num_cols = form.get("num_cols")
    autofill = form.get("autofill")

    # set defaults, to be overriden
    mycontext["set_rows"] = 7
    mycontext["set_cols"] = 7
    mycontext["prefill"] = ""
    mycontext["final_output"] = "grid editor"

    # override defaults, if dimensions provided
    if num_rows:
        mycontext["set_rows"] = int(num_rows)
    if num_cols:
        mycontext["set_cols"] = int(num_cols)
    if autofill:
        mycontext["prefill"] = autofill

    # deal with possible input
    individual_bubbles_list = []

    # step 0: get everything into one list and into integers when necessary.
    for key, value in form.items():
        if key[0:5] != "point":
            continue

        key = key.replace("point", "")
        key = [int(i) for i in key.split(",")]

        individual_bubbles_list.append((key, value))

    rows_list = []
    # default row size to define the variable
    row_size = 8

    # figure out row length by finding the end of the first row
    for i, bubble in enumerate(individual_bubbles_list):
        if bubble[0][0] < individual_bubbles_list[i+1][0][0]:
            row_size = bubble[0][1] + 1
            break

    # create rows with only the bubble content
    for i in range(0, len(individual_bubbles_list), row_size):
        bloated_row = individual_bubbles_list[i:i+row_size]
        filtered_row = [value[1] for value in bloated_row]
        rows_list.append(filtered_row)

    spoilered_rows = []
    for row in rows_list:
        spoilered_rows.append("||" + "||||".join(row) + "||")

    output = "\n".join(spoilered_rows)

    mycontext["final_output"] = output

    return render_template("grid_input.html", context=mycontext)


@app.route("/hello", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        mydata = request.form["mytext"]
        return render_template("hello.html", context={"fill_text": mydata})
    return render_template("hello.html", context={"fill_text": ""})