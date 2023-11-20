from flask import Flask, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

#Home Page
@app.route("/")
def home():
    return render_template("index.html")

#Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

#About Page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)