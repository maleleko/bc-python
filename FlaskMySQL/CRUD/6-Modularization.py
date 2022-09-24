#                       MODULARIZATION

# At first glance it may look like a modularized project is more complicated, but if we were to open up the server.py file the differences will favor the modularized.  It's a way we can organize our code and make our files cleaner to read.  It also gives each file a specific purpose.  Would you rather work at a job where you have multiple duties to perform through your day or just one?


#                   Step 1: The App Folder

                    # The process

    # 1) Create a directory called flask_app
    # 2) Create __init__.py file inside flask_app folder.
    # 3) Insert this code:
        # # __init__.py
        # from flask import Flask
        # app = Flask(__name__)
        # app.secret_key = "shhhhhh"
    
    # 4) Remove above lines from server.py
    # 5) In server.py we add this line:
        # from flask_app import app
    # 6) Move templates folder into flask_app
    # 7) Move static folder into flask_app