from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "why are you trying hackme"


@app.route('/')
def request():
    if 'count' not in session:
        session['count'] = 1
    else: 
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_sesh')
def destroy_sesh():
    session.clear()
    return redirect('/')

@app.route('/two')
def bytwo():
    if 'count' not in session:
        session['count'] = 1
    else: 
        session['count'] += 2
    return render_template('index.html')


#ill play with this later
# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
# @app.route('/specify')
# def specified():
#     if 'count' not in session:
#         session['count'] = 1
#     else:
#         session['count'] = session['count']
#     return render_template('index.html')

# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality


if __name__ == "__main__":
    app.run(debug=True, port=8000)