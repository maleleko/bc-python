from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user


@app.route('/')
def index():
    if "user_id" not in session:
        return render_template("index.html")
    return redirect("/recipes")

# @app.route('/recipes')
# def recipes():
#     if "user_id" not in session:
#         return redirect('/')
#     logged_in_user = user.User.get_user_by_id(session["user_id"])
#     return render_template("recipes.html", logged_in_user = logged_in_user)


@app.route('/register', methods=["POST"])
def register():
    if not user.User.validate_register(request.form):
        return redirect("/")
    user_id = user.User.register(request.form)
    session["user_id"] = user_id
    return redirect("/")

@app.route('/login', methods=["POST"])
def login():
    logged_in_user = user.User.validate_login(request.form)
    if not logged_in_user:
        return redirect("/")
    session["user_id"] = logged_in_user.id
    return redirect("/recipes")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")