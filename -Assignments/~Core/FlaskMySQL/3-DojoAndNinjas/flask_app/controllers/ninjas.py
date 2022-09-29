from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import ninja, dojo


@app.route('/ninjas')
def create_ninja():
    dojos = dojo.Dojo.get_all()
    return render_template('ninjas.html', all_dojos = dojos)

@app.route('/new_ninja', methods=["POST"])
def newninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"]
    }
    ninja.Ninja.save(data)
    return redirect('/dojos')