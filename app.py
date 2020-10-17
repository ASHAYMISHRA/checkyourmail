import os
# import pandas as pd 
# import numpy as np 
import flask
import pickle
from flask import Flask
from flask import render_template , request

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


def mailpredict(text):
	to_predict=[text]
	loaded_model = pickle.load(open("model.pkl","rb"))
	vec_mod=pickle.load(open("vec.pkl","rb"))
	result = loaded_model.predict(vec_mod.transform(to_predict))
	return result


@app.route('/predict',methods = ['POST'])
def predict():
	text=request.form.get('mail')
	algo=request.form.get('algo')
	l=0
	l=len(text.strip())
	if algo=="DTC":
		loaded_model = pickle.load(open("DTC.pkl","rb"))
	elif algo=="KNN":
		loaded_model = pickle.load(open("KNN.pkl","rb"))
	elif algo=='LOG':
		loaded_model = pickle.load(open("LOG.pkl","rb"))
	elif algo=="MNB":
		loaded_model = pickle.load(open("MNB.pkl","rb"))
	elif algo=="RFC":
		loaded_model = pickle.load(open("RFC.pkl","rb"))
	elif algo=="SGD":
		loaded_model = pickle.load(open("SGD.pkl","rb"))
	elif algo=="SVC":
		loaded_model = pickle.load(open("SVC.pkl","rb"))
	else:
		loaded_model = pickle.load(open("model.pkl","rb"))
	to_predict=[text]
	vec_mod=pickle.load(open("vec.pkl","rb"))
	result = loaded_model.predict(vec_mod.transform(to_predict))
	return render_template("index.html",prediction=result[0],algo=algo,textlen=l,text=text)
if __name__=="__main__":
        app.run(debug=True)

