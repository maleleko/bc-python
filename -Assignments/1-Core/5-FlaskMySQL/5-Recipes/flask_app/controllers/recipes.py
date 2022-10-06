from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, recipe


@app.route('/recipes')
def main_page():
    if "user_id" not in session:
        return redirect('/')
    logged_in_user = user.User.get_user_by_id(session["user_id"])
    recipes = recipe.Recipe.get_all_recipes()
    return render_template("recipes.html", logged_in_user = logged_in_user, recipes=recipes)


@app.route('/recipes/new')
def new_recipe():
    if "user_id" not in session:
        return redirect('/')
    logged_in_user = user.User.get_user_by_id(session["user_id"])
    return render_template("new-recipe.html", logged_in_user = logged_in_user)

# # create recipe post method
@app.route('/new-recipe', methods=["POST"])
def create_recipe():
    if "user_id" not in session:
        return redirect('/')
    if recipe.Recipe.validate_recipe(request.form):
        recipe.Recipe.create_recipe(request.form)
        return redirect('/recipes')
    return redirect('/recipes/new')

# show recipe details
@app.route('/recipes/<int:id>')
def view_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    logged_in_user = user.User.get_user_by_id(session["user_id"])
    recipe_to_view = recipe.Recipe.get_recipe(id)
    return render_template('show-recipe.html', logged_in_user = logged_in_user, recipe = recipe_to_view)

# update recipe
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = user.User.get_user_by_id(session["user_id"])
    recipe_to_edit = recipe.Recipe.get_recipe(id)
    return render_template("update-recipe.html", logged_in_user=logged_in_user, recipe=recipe_to_edit)

@app.route('/update-recipe/<int:id>', methods=["POST"])
def update_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    if recipe.Recipe.validate_recipe(request.form):
        recipe.Recipe.update_recipe(request.form)
        return redirect(f"/recipes/{id}")
    return redirect(f"/recipe/edit/{id}")

# delete recipe
@app.route('/delete-recipe/<int:id>')
def delete(id):
    if "user_id" not in session:
        return redirect('/')
    recipe.Recipe.delete_recipe(id)
    return redirect('/recipes')