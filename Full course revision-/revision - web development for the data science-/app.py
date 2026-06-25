from flask import Flask,render_template,request
#basic minimal flask app 
app = Flask(__name__ , static_folder='static',static_url_path="Data science learning\Full course revision-\revision - web development for the data science-\static")

@app.route("/")
def hello_world():
    return 'Hello_world'
    # return render_template('HTML_REVISION.html')

#topic = Query parameter

@app.route("/predict")
def predict():#quering  parameter
    x = request.args.get('x')#requesting the value fron the url 
    y = request.args.get('y')#requesting the value of the y from the url 

    return f"x = {x}, y = {y}"

@app.route("/prediction.predict")#app route prediction 
def prediction ():
    feature = request.args.get('value')#requesting value from the url 
    if not feature:#handling the error 
        return"Value not provided"
    return f"The predicition from the input is {feature}"#returning this on the app interface 
    
#serving the static file on the main website - css files , java files and other images and media 
#changing the location of the static files


#form - user input  for the prediction 
@app.route("/prediction")
def prediction1():
    return render_template ("HTML_REVISION.html")
@app.route("/prediction", method = ["POST"])
def prediction():
    value = request.form('feature')
    return f"Recived value :{value}"



app.run(debug=True)