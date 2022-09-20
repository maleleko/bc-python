from flask import Flask, render_template

app = Flask(__name__)

# Have the root route render a template with a checkerboard on it
@app.route('/')
def checkerboard():
    return render_template('index.html', num=8, num2=8, color1="red", color2="black")

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route('/<int:num>')
def pagetwo(num):
    return render_template('index.html', num=num, num2=8, color1="red", color2="black")

# NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:num>/<int:num2>')
def ninjabonus(num, num2):
    return render_template('index.html', num=num, num2=num2, color1="red", color2="black")


# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:num>/<int:num2>/<string:color1>/<string:color2>')
def senseibonus(num, num2, color1, color2):
    return render_template('index.html', num=num, num2=num2, color1=color1, color2=color2)

if __name__ =="__main__":
    app.run(debug=True, port=8000)