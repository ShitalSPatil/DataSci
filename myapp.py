from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def get_result():
  poly=pickle.load(open('poly.pkl','rb'))
  model=pickle.load(open('model.pkl','rb'))
  query=[[float(request.form['Experience'])]]
  X_query=poly.transform(query)
  sal1=model.predict(X_query)
  #use model.predict to predict salary

  return 'Dear' +request.form["Name"]+'YourPredicted salary after'+request.form["Experience"]+'Experience is:'+str(sal1);
if __name__=='__main__':
  app.run(debug=True)

