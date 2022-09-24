#                           CONTROLLERS


# Now that we have our flask_app module set up with templates and static folders inside, we now need to move all of the code from our server.py into it, and organize it with purpose.


                # The Process

    # 1) Create "config" and "controllers" folders into flask_app folder.
    # 2) Move mysqlconnection.py into config folder.
    # 3) Create a .py file named after what ever we are controlling in a pluralization form.
    # 4) Move all the @app.route functions into the controller file.
    # 5) Insert this code in burgers.py:
        # from flask_app import app
        # from flask import render_template,redirect,request,session,flash
        # from burger import Burger
    # 6) Remove above lines from server.py
    # 7) In server.py we add this line:
        # from flask_app.controllers import burgers