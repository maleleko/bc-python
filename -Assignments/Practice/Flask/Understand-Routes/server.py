from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world"

@app.route('/dojo')
def saydojo():
    return 'dojo'

@app.route('/say/<string:name>')
def saysumn(name):
    return "hi, " + name

@app.route('/repeat/<int:num>/<string:phrase>')
def repeatint(num, phrase):
    test = " "
    for i in range(0,num):
        test += phrase + " "
    return test

@app.errorhandler(404)
def sorry(e):
    return "Sorry! No response! Try again.", 404


if __name__=="__main__":
    app.run(debug=True, port=8000)