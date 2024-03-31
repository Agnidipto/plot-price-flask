import tensorflow as tf
import numpy as np
import json

from exceptions import ModelNotLoaded

class Predictions() :
  
  def __init__(self) -> None:
    self.model = None
    self.data_columns = None

  def load_model(self) :

    if self.model != None :
      return "Model already Loaded!"
    
    self.model = tf.keras.models.load_model('my_model.keras')

    with open('columns.json', 'r') as file:
        # Load the JSON data into a dictionary
        data_dict = json.load(file)

    self.data_columns = data_dict['data_columns']

    return "Model Loaded Successfully!"

  def get_predictions(self, data: dict) :

      print(type(self.model))

      if self.model == None :
        raise ModelNotLoaded()

      X = np.zeros(len(self.data_columns))

      X[0] = data.get('boundary', 0)
      X[1] = data.get('construction', 0) # quite weird
      X[2] = data.get('floor', 2)
      X[3] = data.get('open_sides', 2) # quite weird
      X[4] = data.get('garden_park', 0)
      X[5] = data.get('main_road', 0)
      X[6] = data.get('pool', 0) # don't use
      X[7] = data.get('width_road', 10) 
      X[8] = data.get('area', 1440)
      X[9] = data.get('new_property', 1)

      X[10] = X[7] * X[3] # width_open
      X[11] = X[2] / X[8] # floor_by_area
      X[12] = X[2] / X[7] # floor_by_width

      area_mean, area_std = 7.652456222450403, 0.8221394216377748
      width_mean, width_std = 2.250238284146862 , 0.6616294390712966
      width_open_mean, width_open_std = 2.8180932169586836 , 0.7954702674245552
      floor_by_area_mean, floor_by_area_std = -1.9187939331933004 , 0.9169052779150308
      floor_by_width_mean, floor_by_width_std =  -1.1204044099254058 , 0.6956414037035519

      X[8]  = (np.log(X[8] ) - area_mean) / area_std
      X[7]  = (np.log(X[7] ) - width_mean) / width_std
      X[10] = (np.log(X[10]) - width_open_mean) / width_open_std
      X[11] = (np.log(X[11]) - floor_by_area_mean) / floor_by_area_std
      X[12] = (np.log(X[12]) - floor_by_width_mean) / floor_by_width_std

      ## Location

      if 'location' in data :
          for location in data['location'] :
              loc_idx = self.data_columns.index(location)
              X[loc_idx] = 1
      else :
          loc_idx = loc_idx = self.data_columns.index('Rajarhat')
          X[loc_idx] = 1

      print(np.sum(X[13:]))

      X_reshape = X.reshape(1, -1)

      return self.model.predict(X_reshape)[0][0]
  
