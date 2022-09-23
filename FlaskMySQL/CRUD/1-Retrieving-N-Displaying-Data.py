#                       Retrieving and Displaying Data

# When the user visits the root route, we want to display all the friends, so our logic will include fetching all the friends from the database, and then rendering that data onto our template.

# first_flask_mysql/server.py
    # @app.route('/')
    # def index():
    #     friends = Friend.get_all()
    #     print(friends)
    #     return render_template("index.html", all_friends = friends)

# Then in our template:
# first_flask_mysql/templates/index.html
    # <h1>All My Friends</h1>
    # {% for one_friend in all_friends %}
    #     <p>First Name: {{one_friend.first_name}}</p>
    #     <p>Last Name: {{one_friend.last_name}}</p>
    #     <p>Occupation: {{one_friend.occupation}}</p>
    #     <hr>
    # {% endfor %}
