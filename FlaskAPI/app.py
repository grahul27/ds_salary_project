import flask
from flask import Flask,jsonify,request
import json
import pickle

app=Flask(__name__)
@app.route('/predict',methods=['GET'])

def load_model():
    file__name='model_file.p'
    with open(file__name,'rb') as pickled:
        data=pickle.load(pickled)
        model=data['model']
    return model


def predict():
    response=json.dumps({'response':'hello'})
    return response, 200

if __name__name__=='__main__':
    application.run(debug=True)