from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import dojo


@app.route("/")
def index():
    return redirect('/dojos')

@app.route('/dojos')
def our_dojos():
    dojos = dojo.Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos = dojos)

@app.route('/new_dojo', methods=["POST"])
def newdojo():
    data = {
        "name": request.form["name"]
    }
    dojo.Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojos(id):
    data = {
        "id":id
    }
    dojo_with_ninjas = dojo.Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo.html", dojo = dojo_with_ninjas)