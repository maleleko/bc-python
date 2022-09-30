from flask import Flask, render_template, request, redirect, session #added request

app = Flask(__name__)
#adding secret key from sessions reading
app.secret_key = 'keep it secret, keep it safe.' #set a secret key for security

@app.route('/')
def index():
    return render_template('index.html')

#making this method from post form submission reading on platform
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # name = request.form['name'] #added from redirecting
    # email = request.form['email'] #added from redirecting

    #adding to the vars above from session reading
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    #  Never render a template on a POST request.
    #  Instead we will redirect to our index route.
    return redirect("/show")

#adding this method from redirect reading on platform
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail']) #modified from session reading on platform

if __name__=="__main__":
    app.run(debug=True, port=8001)