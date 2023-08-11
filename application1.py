import os
from tensorflow.keras.models import load_model
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import sklearn
import pandas as pd
list1=[]
app=Flask(_name_)
base_dir=os.path.dirname(os.path.abspath(_file_))
model=load_model(os.path.join(base_dir,"model.hdf5"))
@app.route('/')
def home ():
  return render_template("index.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
  global result
  if request.method=='POST':
    time=request.form['time']
    v1=request.form['V1']
    v2= request.form['V2']
    v3= request.form['V3']
    v4= request.form['V4']
    v5= request.form['V5']
    v6= request.form['V6']
    v7= request.form['V7']
    v8= request.form['V8']
    v9= request.form['V9']
    v10= request.form['V10']
    v11= request.form['V11']
    v12= request.form['V12']
    v13= request.form['V13']
    v14= request.form['V14']
    v15= request.form['V15']
    v16= request.form['V16']
    v17= request.form['V17']
    v18= request.form['V18']
    v19= request.form['V19']
    v20= request.form['V20']
    v21= request.form['V21']
    v22= request.form['V22']
    v23= request.form['V23']
    v24= request.form['V24']
    v25= request.form['V25']
    v26= request.form['V26']
    v27 = request.form['V27']
    v28 = request.form['V28']
    amount=request.form['amt']
    base_dir = os.path.dirname(os.path.abspath(_file_))
    model = load_model(os.path.join(base_dir, "model.hdf5"))
    result=model.predict([[float(time),float(v1),float(v2),float(v3),float(v4),float(v5),float(v6),float(v7)
                            ,float(v8),float(v9),float(v10),float(v11),float(12),float(v13),float(v14),float(v15),
                           float(v16),float(v17),float(v18),float(v19),float(v20),float(v21),float(v22),float(v23),float(v24),float(v25),float(v26)
                                  ,float(v27),float(v28),float(amount)]])
    if int(result[0])==1:
      prediction="Given Transaction is Fraudulent"
    else:
      prediction="Given Transaction is Genuine/Non-Fraudulent"
    return render_template("result.html",prediction=prediction)
if _name=='main_':
    app.debug=True
    app.run()