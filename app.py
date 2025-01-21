from flask import Flask, request, render_template
import numpy as np
import pandas
import sklearn
import pickle

#importing model
model=pickle.load(open('model.pkl','rb'))

#creation of flask app
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])
    feature_list=[N,P,K,temp,humidity,ph,rainfall]
    single_pred=np.array(feature_list).reshape(1,-1) #to get a single row
    prediction=model.predict(single_pred)
    crop_dict = {
        1: 'rice',
        2: 'maize',
        3: 'jute',
        4: 'cotton',
        5: 'coconut',
        6: 'papaya',
        7: 'orange',
        8: 'apple',
        9: 'muskmelon',
        10: 'watermelon',
        11: 'grapes',
        12: 'mango',
        13: 'banana',
        14: 'pomegranate',
        15: 'lentil',
        16: 'blackgram',
        17: 'mungbean',
        18: 'mothbeans',
        19: 'pigeonpeas',
        20: 'kidneybeans',
        21: 'chickpea',
        22: 'coffee'
    }
    p=int(prediction[0])
    if p in crop_dict:
        crop = crop_dict[p]
        result = "{} is the best crop to be cultivated".format(crop)
    else:
        result = "We are unable to recommend a proper crop for this environment"
    return render_template('index.html',result=result)

# python name
if __name__=="__main__":
    app.run(debug=True)
