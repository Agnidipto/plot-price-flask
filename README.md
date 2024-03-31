# Kolkata Land Price Prediction

This Flask web application uses a Neural Network model built with TensorFlow to predict the price of a plot of land in Kolkata. It provides three API endpoints:

1. **Load Model Endpoint**
   - **Method**: GET
   - **URL**: `/`
   - **Description**: This endpoint loads the trained TensorFlow model for land price prediction.

2. **Test Model Endpoint**
   - **Method**: GET
   - **URL**: `/test`
   - **Description**: This endpoint tests the loaded model using predefined inputs and returns the predicted prices.

3. **Predict Price Endpoint**
   - **Method**: POST
   - **URL**: `/predict`
   - **Description**: This endpoint accepts user inputs (such as area and location) via a JSON payload sent in a POST request. It then predicts and returns the price based on the provided inputs.

## Usage

1. **Install Dependencies**
   - Make sure you have all the dependencies installed. You can install them using the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Flask App**
   - Start the Flask application by running:
     ```bash
     python app.py
     ```

3. **Load the Model**
   - Access the `/` endpoint to load the TensorFlow model.

4. **Test the Model**
   - Access the `/test` endpoint to test the model with predefined inputs.

5. **Predict Land Price**
   - Send a POST request to the `/predict` endpoint with user inputs in JSON format. The inputs should include parameters like 'area' and 'location'.

## Example

### Test Model Endpoint

Send a GET request to `/test`:
```bash
curl http://127.0.0.1:5000/test
```

### Predict Price Endpoint

Send a POST request to /predict with JSON payload:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"area": 1000, "location": "["Joka"]"}' http://127.0.0.1:5000/predict
```
