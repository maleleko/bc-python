                        # Static files

# Static content is any content that can be served up to the client without being modified, generated, or processed by the server.
# Flask serves static content from a directory called static.
# Much like our templates directory, the static directory must be called static
    # used to serve all of your stylesheets, images, and JavaScript files



#  Now, say we placed a CSS file, a JavaScript file, and an image directly into our static folder.
        # in our HTML file we put
    # <!-- based on the folder structure on the right -->
    # <!-- linking a css style sheet -->
    # <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
    # <!-- linking a javascript file -->
    # <script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
    # <!-- linking an image -->
    # <img src="{{ url_for('static', filename='my_img.png') }}">



                        # Organization

# It is common to create a few more folders to organize our static files into categories according to document type.
# We can call them css, js, and img and house the corresponding files in the different folders. 
        # to do this, link it.

    # <!-- linking a css style sheet -->
    # <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style.css') }}">

    # <!-- linking a javascript file -->
    # <script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>

    # <!-- linking an image -->
    # <img src="{{ url_for('static', filename='img/my_img.png') }}">



            # When using static files, your browser will likely cache them. If you are making changes in static files and they don't appear to be updating, do a hard refresh of the page in your browser: ctrl + shift + r (Windows) or cmd + shift + r (Mac).