from get_predictions import Predictions
from flask import Flask, request, jsonify
from exceptions import ModelNotLoaded
from flask_cors import cross_origin
import json

from exceptions import CannotLoadLocations

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

Predictions = Predictions()

@app.route('/') 
@cross_origin()
def init() :
  try :
    message = Predictions.load_model()
    return jsonify({
      "message" : message
    })
  except Exception as e:
    return jsonify({
      "error" : "An Error Occured!",
      "exception" : str(e)
    }), 500

@app.route('/test')
@cross_origin()
def test_predictions() :
  
  data = {
      'area' : 1440,
      'location' : ['Rajarhat']
  }
  
  try :
    output = Predictions.get_predictions(data) * data.get('area', 1440)
    return jsonify({
      'price' : output
    })

  except Exception as e :
    return jsonify({
      "error" : "An Error Occured!",
      "exception" : str(e)
    }), 500
  
@app.route('/predict', methods = ['POST'])
@cross_origin()
def predict() :
  try :
    data = request.json
    output = Predictions.get_predictions(data) * data.get('area', 1440)
    return jsonify({
      'price' : output
    })
  
  except Exception as e :
    return jsonify({
      "error" : "An Error Occured!",
      "exception" : str(e)
    }), 500
    
@app.route('/locations')
@cross_origin()
def get_locations() :
  try :
    with open('api/locations.json', 'r') as file :
      data = json.load(file)
      return jsonify(data['locations'])
  except Exception as e :
    return jsonify({
      "error" : "An Error Occured!",
      "exception" : str(e)
    }), 500

if __name__ == '__main__' :
  app.run(debug=True)