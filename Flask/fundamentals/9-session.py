# Remember back to algorithms and the Python Fundamentals chapter--when we had several functions in the same file, did they know anything about each other? Nope! It is no different here--each method that is handling a route doesn't know anything about any of the other routes.

# Here's the thing about the HTTP request/response cycle: it is stateless. That means that each request/response cycle is independent and ignorant of all other requests, before or after. Because we made a second request (by redirecting) after the client posted data in the form, the browser only knows about the second request we made (in our case, the GET request to the "/show" route). Because the form data was part of the first request, the second request has no access to it.

# But certainly this is not our experience in the real world--when we go shopping online, the site seems to remember who we are, what items are in our shopping cart, etc. (Even other sites know what we've been shopping for! Creepy, right?) This is because many sites make use of persistent data storage! One form of persistence is session.


            # What is session?
# With session, we can establish a relationship with the client by saving, or writing, certain valuable pieces of data for use in future cycles, and by reading that data we've stored in previous cycles. This opens up a new world of user experience. With session, the user can have a conversation of sorts with a website, where a user makes decisions that can be tracked so the server can create a more cohesive user experience.

# In a given process (HTTP request/response), we can manage data (search terms and search results for instance) that outlives the process that generated it. This data is called state. State allows our site to "know" a lot of useful information, like:

        # Whether there is a user logged in
        # Who the current user is
        # What links a user has viewed previously


# We get to decide what to save about our clients. Session is a tool for us, as developers, to use to our advantage. In the same way we create variables in our functions to help us solve problems, we keep state data in session to help us solve problems down the line, i.e. in subsequent HTTP requests.

# Persistent data storage helps us bridge the gap between a stateless protocol like HTTP with the stateful data generated through it. This is at the heart of the modern web and is heavily used by web developers around the world.

# Very shortly, we'll also discuss databases as another tool for persistent data storage. When we start incorporating a database into our projects, we'll consider what distinct roles each of these tools serve. We should not abuse the amount of information we store in session. Store only what you need. Once we incorporate a database, we should be limiting what we store in session.

#       A Note on Cookies
# You've probably heard of the term cookies before. Some frameworks, including Flask, use cookies to store session data. Flask uses secure hashing of session data to send a packet of information from server to client. This packet is known as a cookie. Once a client's browser has received this cookie, it writes the information contained in it to a small file on their hard drive.
# While hashed, cookies are not incredibly secure, so don't save anything private in them.

# Setting Up Session in Flask
    # from flask import Flask, render_template, request, redirect, session
# To use sessions in Flask, we are also required to give our app a secret key:
# https://flask.palletsprojects.com/en/2.1.x/config/#SECRET_KEY

# Because the create_user method is the method in which we receive the information from the POST request, let's write the information to session in this method:

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')


# Previously in our show_user function, we didn't have access to the name and email from the form submission. Now, because of session, we have a way to access the name and email in a different function!

# let's modify our show_user function

# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])




                # Session in templates 
# Right now we are passing the information stored in session to the templates using named arguments. Session data is also available directly in our templates. That means we can do this:

# @app.route('/show')
# def show_user():
#     return render_template('show.html')

# show.html
    # <h1>User:</h1>
    # <h3>{{session['username']}}</h3>
    # <h3>{{session['useremail']}}</h3>

