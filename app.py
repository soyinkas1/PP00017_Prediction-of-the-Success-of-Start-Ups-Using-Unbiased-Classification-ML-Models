from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

app =  Flask(__name__)

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method== 'GET':
        return render_template('home.html')
    else:
        data= CustomData(
            yrs_of_operation=request.formm.get('yrs_of_operation'),
            yrs_since_last_funding=request.form.get('yrs_since_last_funding'),
            degree_length=request.form.get('degree_length'),
            per_exp_at_coy_start=request.form.get('per_exp_at_coy_start'),
            sponsor=request.form.get('sponsor'),
            speaker=request.form.get('speaker'),
            organizer=request.form.get('organizer'),
            exhibitor=request.form.get('exhibitor'),
            employee_count=request.form.get('employee_count'),
            total_funding_usd=request.form.get('total_funding_usd')






        )