from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def initial():
    return render_template('index.html')

@app.route('/play')
def pageone():
    return render_template('indexplay.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)