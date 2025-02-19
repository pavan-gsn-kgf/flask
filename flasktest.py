
# Data Dump in SQLite
import pandas as pd 
from flask import Flask, jsonify,send_file,make_response, render_template, request, redirect, url_for, session
from flask_cors import CORS, cross_origin
import logging
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
CORS(app, origins="http://localhost:5000", supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
app.secret_key = 'SOP'  # Change this to a random secret key


def dropdown():
    models=['Seasonal Forecast', 'ESM','Moving Average']

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
    return models,month_order
model,mon = dropdown()


# model, custgrp,zone,sku,seg,dist = dropdown()
@app.route('/model', methods=['POST','GET'])
@cross_origin()
def option1():
    option = [{"id": i + 1, "name": x} for i, x in enumerate(model)]
    return jsonify({"model": option})

@app.route('/month', methods=['POST','GET'])
@cross_origin()
def option2():
    # print(sku)
    option = [{"id": i + 1, "name": x} for i, x in enumerate(mon)]
    return jsonify({"sku": option})



if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0' , port = 5000)
