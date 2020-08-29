from flask import Flask, request, jsonify
import os
import torch
from frontend import *


app = Flask(__name__)

@app.route('/predict')
def predict():
	try:
		camfeed_inference("weights/weights.pth", 'cpu')
	except:
		return jsonify({"error":'1'})

	return jsonify({'result': 1})



if __name__ == '__main__':
	app.run()