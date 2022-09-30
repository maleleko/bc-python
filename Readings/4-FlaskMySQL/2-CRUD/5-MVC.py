#               MVC

# Developers who design frameworks have to make decisions about organizing code. One of the most popular patterns for organizing code is one known as MVC: Model-View-Controller.  Here's a basic breakdown of responsibilities:

# Model
    # 1) may build database tables
    # 2) handles logic that relies on data
    # 3) interfaces with the database

# View
    # 1) HTML page that gets served to the client
    # 2) may contain some logic to be handled by a template engine

# Controller
    # 1) receives incoming requests
    # 2) minimal logic
    # 3) calls on models to aggregate/process data
    # 4 determines appropriate response



                # Modularizing Application

# Some web development frameworks combine everything into one large, potentially monstrous file.
#  Imagine you're on a team with a dozen other developers—how easy will it be to collaborate in one giant file? Yikes! Using the MVC pattern allows us to outsource the different kinds of tasks to specific file locations.
# When we begin a Flask project, we will need to created files to play all of the necessary roles in a web application:\

    # Routes(expected requests)
    # Functions, associated with those routes(how our server responds)
    # Database interaction through our models(storing, retrieving data from database)
    # templates  (what the user interacts with)