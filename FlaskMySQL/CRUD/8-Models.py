                    # MODELS

        # Key take aways
            # 1) We are going to use our OOP skills to to make classes that correspond to our database tables.
            # 2) We use these classes to query and map the raw data coming from the database into objects.
            # 3) Our controller file will only handle rendering and rerouting and calling on the Model class to deal with the database.

        # The process
        # 1) Create models folder inside flask_app folder.
        # 2) Move the burger.py file into the models.
        # 3) Change the import statement in burger.py :
            # from flask_app.config.mysqlconnection import connectToMySQL
            # # burger.py
            # class Burger:
            #     def __init__(self,data):
            #         self.id = data['id']
            #         self.name = data['name']
            #         self.bun = data['bun']
            #         self.meat = data['meat']
            #         self.calories = data['calories']
            #         self.created_at = data['created_at']
            #         self.updated_at = data['updated_at']

        # 4) Have the controller call the Model class methods.

        # 5) Update the Burger import statement in the controller.



                    # Splitting up the tasks between Models and Controllers

# We now have the task of splitting up the logic between querying the database and handling things like routing and rendering templates. We use @classmethod when we want to query the database.

                # Getting All Burgers

        # Controllers 

    # # burgers.py...
    # from flask_app.models.burger import Burger
    # # gets all the burgers and returns them in a list of burger objects .
    # @app.route('/burgers')
    # def burgers():
    # 	return render_template('results.html',burgers=Burger.get_all())

        # Models:
    # burger.py...
    # gets all the burgers and returns them in a list of burger objects .
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM burgers"
    #     burgers_from_db = connectToMySQL('burgers').query_db(query)
    #     burgers = []
    #     for b in burgers_from_db:
    #         burgers.append(cls(b))
    #     return burgers


                # Creating A Burger

        # Controllers:
    # burgers.py...
    # from flask_app.models.burger import Burger
    # # gets all the burgers and returns them in a list of burger objects .
    # @app.route('/create/burger',methods=['POST'])
    # def create_burger():
    #     data = {
    #             "name" : request.form['name'],
    #             "bun" : request.form['bun'],
    #             "meat" : request.form['meat'],
    #             "calories" : request.form['calories']
    #     }
    #     Burger.save(data)
    #     return redirect('/burgers')



        # Models 
    # burger.py...
    # # gets all the burgers and returns them in a list of burger objects .
    # @classmethod
    # def save(cls,data):
    #     query = "Insert INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
    #     burger_id = connectToMySQL('burgers').query_db(query,data)
    #     return burger_id