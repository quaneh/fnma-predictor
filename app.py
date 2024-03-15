from flask import Flask, jsonify, request
import pandas as pd
import pickle
import numpy as np
import xgboost as xgb

from data_model.application_details import ApplicationDetails, ApplicationDetailsSchema

app = Flask(__name__)

with open('default_predictor_xgb.pkl', 'rb') as f:
    prediction_model = pickle.load(f)

@app.route('/')
def hi_there():
    return 'Predictor Model Ready!'


@app.route("/predict")
def predict_default():

    application_details = ApplicationDetailsSchema().load(request.get_json())

    entry = pd.DataFrame.from_dict([application_details], orient='columns')

    # Extract text features
    cats = entry.select_dtypes(exclude=np.number).columns.tolist()

    # Convert to Pandas category
    for col in cats:
        entry[col] = entry[col].astype('category')

    dm_entry = xgb.DMatrix(entry, enable_categorical=True)

    print(prediction_model.predict(dm_entry))

    return {'default_probability': str(prediction_model.predict(dm_entry)[0])}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)