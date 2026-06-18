from flask import Flask,render_template
from flask import Flask
import pandas as pd 

app = Flask(__name__,static_folder='static files',static_url_path='/files')

@app.route("/")
def hello_world():
    name  = 'JILL'
    language = "Python"
    intro = 'My name is monu verma i am going to be the best ai programmer'
    luck_no = [2,3,4,5,12,4,33,43,12]
    footer ="<p>Copyright 2025 | All Rights Reserved <p>"
    data_frame = pd.read_csv('csv_updated.csv')
    return render_template ("index.html", name = name, lang = language,intro = intro,lucky_no = luck_no,footer = footer,data_frame = data_frame)

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


