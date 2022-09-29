from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/created_users')

@app.route('/created_users')
def our_user_list():
    users = User.get_all()
    print(users)
    return render_template('create.html', all_users = users)


if __name__ == "__main__":
    app.run(debug=True, port=8000)