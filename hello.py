from flask import Flask, render_template
# languages -> frames

# frontend
# view -> controller
# html, css (scss, css in js, less, sass), javascript

# json format 
# xml

# backend
# database
# api

# model -> database view -> app controller

# export FLASK_ENV=development

# jinja tempating
# https://jinja.palletsprojects.com/en/3.0.x/templates/

# bootstrap
# https://getbootstrap.com/docs/5.0/getting-started/introduction/


app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "yajana"
    return render_template('hello.html', name=name)

@app.route("/user/<name>")
def hello(name):
    return f"Hello, {str(name)}!"

@app.route("/hello")
def say_hello():
    return "<h1>Hello, it's me!</h1>"