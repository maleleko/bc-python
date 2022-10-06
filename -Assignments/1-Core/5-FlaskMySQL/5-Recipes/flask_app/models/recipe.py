from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

class Recipe:
    DB="recipes_erd"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.author = data['author']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name of the Recipe must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if recipe["date_made"] == "":
            flash("Date Made cannot be blank.")
            is_valid = False
        if "under_thirty" not in recipe:
            flash("Does the recipe take less than 30 minutes?")
            is_valid = False
        return is_valid

    @classmethod
    def create_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, author, instruction, under_thirty, date_made, user_id)
        VALUES (%(name)s, %(description)s, %(author)s, %(instruction)s, %(under_thirty)s, %(date_made)s, %(user_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT * from recipes JOIN users on recipes.user_id = users.id ORDER BY recipes.created_at;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            creator = user.User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipes

    @classmethod
    def get_recipe(cls, recipe_id):
        data = {"id": recipe_id}
        query = """
        SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            creator = user.User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipe

    @classmethod
    def update_recipe(cls, data):
        query = """
        UPDATE recipes SET 
        name = %(name)s, author = %(author)s, description = %(description)s, instruction = %(instruction)s, under_thirty = %(under_thirty)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE recipes.id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_recipe(cls, id):
        data = { "id": id }
        query = """
        DELETE FROM recipes WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)