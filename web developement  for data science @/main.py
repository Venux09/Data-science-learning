from flask import Flask,render_template
from flask import Flask

app = Flask(__name__,static_folder='static files',static_url_path='/files')

@app.route("/")
def hello_world():
    name  = 'JILL'
    language = "Python"
    return render_template ("index.html", name = name, lang = language)

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


