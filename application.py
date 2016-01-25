from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Shows an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Shows the application form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
    """Shows a response to confirm submitted application."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary_requirement = request.form.get("salary-requirement")
    
    if request.form.get("position") == "software-eng":
        position = "Software Engineer"
    elif request.form.get("position") == "qa-eng":
        position = "QA Engineer"
    elif request.form.get("position") == "prod-mgr":
        position = "Product Manager"

    print first_name
    print last_name
    print position
    print salary_requirement

    return render_template("application-response.html", 
        first_name=first_name, 
        last_name=last_name,
        position=position, 
        salary_requirement=salary_requirement
        )

if __name__ == "__main__":
    app.run(debug=True)
