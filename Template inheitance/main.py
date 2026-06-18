from flask import Flask, render_template,request

from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args('name', default = 'Unnamed')
    lang  = request.args('lang')
    return render_template('index.html',lang = lang, name = name)


app.run(debug=True)