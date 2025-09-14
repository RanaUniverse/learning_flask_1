from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/user/<int:user_id>")
def user(user_id: int):
    return f"Hello User, Your User Id Is: {user_id}"


@app.route("/user/<string:user_name>")
def user_with_name(user_name: str):
    return f"Hello User, You Have a Username:\n {user_name}"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/demo_form")
def demo_form_get():
    return render_template("demo_form.html")


@app.post("/demo_form")
def demo_form_post():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    question = request.form.get("question")

    return render_template(
        "demo_form_result.html",
        fname=fname,
        lname=lname,
        question=question,
    )


@app.context_processor
def inject_current_year():
    return {"current_year": 2025}
