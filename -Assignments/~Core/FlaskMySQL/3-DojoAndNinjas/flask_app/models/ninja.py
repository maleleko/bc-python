from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo



class Ninja:
    DB="dojo-and-ninjas-schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s);"
        result =  connectToMySQL(cls.DB).query_db(query, data)
        print("*****", result, "******")
        return result

    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja))
        return ninjas