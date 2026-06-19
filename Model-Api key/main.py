from flask import Flask , request , jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('api/predict', methods = ['GET'])

def predict():

    value  = request.args.get('value')
    

    if value is None:
        return jsonify({'error':'missing input'})  , 400 
    


    #replace with the actual model 
    result = int(value)*2 

    return jsonify({
        'input':value,
        'prediction':result
    })


    

# Run the local server if executed directly
if __name__ == "__main__":
    app.run(debug=True)