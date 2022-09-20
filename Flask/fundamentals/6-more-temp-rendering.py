#                   Passing Lists to Jinja

#           hello_flask/server.py


# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     student_info = [
#        {'name' : 'Michael', 'age' : 35},
#        {'name' : 'John', 'age' : 30 },
#        {'name' : 'Mark', 'age' : 25},
#        {'name' : 'KB', 'age' : 27}
#     ]
#     return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


# Then in our template, let's loop through the list by doing something like this:

    # hello_flask/templates/lists.html

    #     <h1>Random Numbers</h1>
    # {% for number in random_numbers %}
    #     <p>{{ number }}</p>
    # {% endfor %}
    # <h1>Students</h1>
    # {% for student in students %}
    #     <p>{{ student['name'] }} - {{ student['age'] }}</p>
    # {% endfor %}
