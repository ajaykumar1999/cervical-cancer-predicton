# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:37:35 2020

@author: motam
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('modelcancerfinal.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features)
    temp=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    a=np.append(final_features,temp)
    b=[a]
    
    
    prediction = model.predict(b)

    output = prediction[0]
    if output==1:
        output='Very low'
    elif output==2:
        output='Low'
    elif output==3:
        output='Medium'
    elif output==4:
        output='High'
    elif output==0:
        output='No'
        

    return render_template('index1.html', prediction_text='{} risk of getting Cervical Cancer'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
