from flask import Flask,render_template
from flask import Flask

app = Flask(__name__,static_folder='static files',static_url_path='/files')

@app.route("/",methods = ["GET","POST"])
def hello_world():
    return render_template('index.html')


app.run(debug=True)