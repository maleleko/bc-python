#               Rendering Views


# Flask server file knows where to find them. In Flask, we must create a directory alongside our server.py file called templates (exactly this word, plural)



#                   /hello_flask/templates/index.html
#               <h1> Hello Flask!</h1>

# Then in our code, we refer to our HTML files like so
# from flask import Flask, render_template  # added render_template!
# app = Flask(__name__)                     

# @app.route('/')                           
# def hello_world():
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html')  

# if __name__=="__main__":
#     app.run(debug=True)                   

