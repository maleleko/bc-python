from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    all_students = [
        {"id": 1, "name": "test", "email": "t@t.com"},
        {"id": 2, "name": "john", "email": "t@t.com"},
        {"id": 3, "name": "jane", "email": "t@t.com"},
    ]
    return render_template("index.html", name="Jack", students = all_students)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    # for mac users (we need to add port=8000)
    # app.run(debug=True, port=8000)
    # windows/macs runs on 5000 by default
    #     these 4 lines are needed to create a server in flask