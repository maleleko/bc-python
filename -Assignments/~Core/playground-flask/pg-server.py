from contextlib import redirect_stderr
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def initial():
    return render_template('index.html')

@app.route('/play')
def pageone():
    return render_template('indexplay.html')

@app.route('/play/<x>')
def pagetwo(x):
    return render_template('indexplayx.html', x = int(x))

@app.route('/play/<x>/<color>')
def pagethree(x, color):
    return render_template('indexplayxcol.html', x = int(x), color=color)

if __name__ == "__main__":
    app.run(debug=True, port=8000) 