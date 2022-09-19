from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', num=8, color1="red", color2="black")


if __name__ =="__main__":
    app.run(debug=True, port=8000)