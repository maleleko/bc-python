from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    DB="dojo-and-ninjas-schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result =  connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("*********GET NINJA WITH DOJO******", results)

        dojos = cls(results[0])
        for nd in results:
            
            ninja_data = {
                "id": nd["ninjas.id"],
                "first_name": nd["first_name"],
                "last_name": nd["last_name"],
                "age": nd["age"],
                "created_at": nd["ninjas.created_at"],
                "updated_at": nd["ninjas.updated_at"]
            }

            dojos.ninjas.append( ninja.Ninja(ninja_data) )
        return dojos
