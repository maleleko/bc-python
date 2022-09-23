from unicodedata import name
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "not today bucko"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processform():
    # if 'forms' in session:
    #     forms = session['forms']
    # else:
    session['forms'] = [request.form]
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('results.html')

@app.route('/destroy_sesh')
def destroy_sesh():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)