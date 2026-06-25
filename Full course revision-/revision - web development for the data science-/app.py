from flask import Flask,render_template,request, flash, redirect







#basic minimal flask app 
app = Flask("__name__ ")
app.secret_key = '12345'


@app.route("/")
def hello_world():
    feature = 5
    
    
    #process predition here
    flash('Prediction completed')
    return redirect('/')
    

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
# @app.route("/prediction")
# def prediction1():
#     return render_template ("HTML_REVISION.html")
# @app.route("/prediction", method = ["POST"])
# def prediction():
#     value = request.form('feature')
#     return f"Recived value :{value}"

@app.route("/jinja")
def variable():
    value = request.args.get(value)


    return render_template('html.html',prediction = value)

# @app.route("/")


# @app.route('/about page')
# def about_page ():
#     feature = 5
#     if not feature:
#         flash("Enter a value")
#         return redirect('/')
    
#     #process predition here
#     flash('Prediction completed')
#     return redirect('/')#returning the flash message to the home page where hellow world is written 
    




app.run(debug=True)