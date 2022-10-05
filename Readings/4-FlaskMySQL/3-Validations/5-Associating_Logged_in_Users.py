# Users can now register and log back into our application. You have learned how to use session to capture the logged in User’s id in order to display their name on a dashboard page, and make sure that logged-in Users are the only people allowed to use our application. As long as we have their id in session, we can always specify a particular User from the database.

# When you make a tweet on Twitter, or a post on Instagram, you (the logged-in User) are associated with that specific content, so that your friends and followers can see that you made a recent update. How is this done in the back-end though?

# The answer is with a foreign key, which if you recall, is a reference to another table in a database. When you make a Tweet, a foreign key that refers to you as a User is needed to create that Tweet in the database. How do we create this reference? We can use the id (primary key) of you that is being stored in session! This is a good reference because your id as a User should be unique, and refer to only you.

# If Twitter was contained in a Flask application, perhaps some code to create a Tweet would look like this:


# controllers/tweets.py

# @app.route('/tweet/create', methods=["POST"])
# def createTweet():
#     # Validations here...
#     data = {
#         "content": request.form['content'],
#         "location": request.form['location'],
#         # Pass in the id of the User in session to use as the foreign key to describe who made the Tweet
#         "user_id": session['user_id']
#     }
#     Tweet.save(data)
#     # ...

