#           Passing Data to the HTML

#  Notice that in our render_template function call, we are now passing three arguments!

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="hello", times=5)	
#       # notice the 2 new named arguments!
# if __name__=="__main__":
#     app.run(debug=True)



                #    Rendering Data on a Template

# Now how do we use that data on the HTML? There are 2 special inputs we can use to insert Python-like code into our Flask templates.
        # {{ some variable }}
        # {% some expression %}

# update the index.html file
        # <h3>My Flask Template</h3>
        # <p>Phrase: {{ phrase }}</p>
        # <p>Times: {{ times }}</p

        # {% for x in range(0,times): %}
        #     <p>{{ phrase }}</p>
        # {% endfor %}

        # {% if phrase == "hello" %}
        #   <p>The phrase says hello</p>
        # {% endif %}

