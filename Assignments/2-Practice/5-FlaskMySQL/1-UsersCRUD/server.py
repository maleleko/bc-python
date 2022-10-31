from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)


@app.route('/')
def our_users():
    return redirect('/created_users')

@app.route('/create_user')
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

@app.route('/created_users/<int:id>')
def show_user(id):
    data = { 
        "id":id
    } 
    return render_template('show.html', one_user = User.get_id(data))

@app.route('/created_users/edit/<int:id>')
def edit_user(id):
    data = { 
        "id":id
    }   
    return render_template('edit.html', one_user=User.get_id(data))

@app.route('/created_users/edit', methods=['POST'])
def edit():
    User.edit_user(request.form)
    return redirect('/created_users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/created_users')


if __name__ == "__main__":
    app.run(debug=True, port=8000)