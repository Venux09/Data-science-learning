from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('HTML_REVISION.html')


app.run(debug=True)