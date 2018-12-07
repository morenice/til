from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/hello")
def hello_world():
    return "hello flask :)"


@app.route("/users/<username>")
def users(username):
    return "user: {0}".format(username)

@app.route("/posts/<int:pid>")
def posts(pid):
    return "post: {0}".format(pid)
