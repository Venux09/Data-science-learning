from flask import Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World I am monu verma and i am understanding the flask !</p>"

@app.route("/about")
def about():
    return "<p>yo onnesan this is about page!</p>"

@app.route("/contact")
def contact():
    return "<p>This is the page which is realted to the contacts  !</p>"




app.run(debug=True)