#                   Creating our Virtual Environment and Installing Flask

# Now that we have pipenv installed, let's create a new project folder. Using the folder structure we created on day one, create a new folder inside the python_/flask/fundamentals folder called hello_flask.

# Once we are in the project folder we can use pipenv to install Flask
    #run pipenv install flask | to install flask into our project we're working on

# The first time we run pipenv install, it will create 2 files for us, Pipfile and Pipfile.lock. Both are needed in order to use the installed packages, but difference between the two include: Pipfile will display the packages installed, and Pipfile.lock will have the specific details on what version is being used.

    # ***NOTE*** If your receive an error using pipenv, you may need to import it as a module first before it can be run as a script. You can do so using the -m flag as below. You will need to do this every time you use pipenv.

        # Windows: python -m pipenv <command to use>
        # Mac: python3 -m pipenv <command to use>



#                   Activating our Virtual Environment
# Once we have installed the Flask package, we need to activate our environment in order to use it. We can achieve this with the following command.
        # pipenv shell



#                   Checking What's Installed with pip list

# To check what is installed in your virtual environment, with your virtual environment activated (pipenv shell), you can type the command, pip list and you will see a list of what is currently installed. For instance if you wanted to verify for a particular project that you have Flask installed you would activate your environment then use this command as shown below.
    # pip list




#                   Deactivating our Virtual Environment

#exit(lol)


#                    **IMPORTANT DISCLAIMER**
# Do not create a virtual environment within another virtual environment.
