from get_predictions import Predictions
from flask import Flask, request
from exceptions import ModelNotLoaded

app = Flask(__name__)

Predictions = Predictions()

@app.route('/') 
def init() :
  try :
    message = Predictions.load_model()
    return {
      "message" : message
    }
  except :
    return {
      "error" : "Failed to load Model"
    }

@app.route('/test')
def test_predictions() :
  
  data = {
      'area' : 1000,
      'location' : ['Rajarhat']
  }
  
  try :
    output = str(Predictions.get_predictions(data) * data.get('area', 1440))
    return {
      'price' : output
    }

  except Exception as e :
    return {
      "error" : "An Error Occured!",
      "exception" : e.message
    }
  
@app.route('/predict', methods = ['POST'])
def predict() :
  try :
    data = request.json
    output = str(Predictions.get_predictions(data) * data.get('area', 1440))
    return {
      'price' : output
    }
  
  except Exception as e :
    return {
      "error" : "An Error Occured!",
      "exception" : e.message
    }

if __name__ == '__main__' :
  app.run(debug=True)