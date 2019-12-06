from flask import Flask, render_template, request, redirect, url_for
import shelve

app = Flask(__name__, static_folder="static")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sigin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()
