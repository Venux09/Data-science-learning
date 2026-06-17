from flask import Flask,render_template
from flask import Flask

app = Flask(__name__,static_folder='static files',static_url_path='/files')

@app.route("/")
def hello_world():
    return "<p>Hello, World I am monu verma and i am understanding the flask !</p>"

@app.route("/about")
def about():

    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/index")
def index():
    return render_template('index.html')



app.run(debug=True)