from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, UTC
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

app =  Flask(__name__)
Bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "kokoroasiri"

## Route for a home page

class WebForm(FlaskForm):
    yrs_of_operation = IntegerField('yrs_of_operation', validators=[DataRequired()])
    yrs_since_last_funding = IntegerField('yrs_since_last_funding', validators=[DataRequired()])
    per_exp_at_coy_start = IntegerField('per_exp_at_coy_start', validators=[DataRequired()])
    sponsor = IntegerField('sponsor', validators=[DataRequired()])
    speaker = IntegerField('speaker', validators=[DataRequired()])
    organizer = IntegerField('organizer', validators=[DataRequired()])
    exhibitor = IntegerField('exhibitor', validators=[DataRequired()])
    employee_count = IntegerField('employee_count', validators=[DataRequired()])
    total_funding_usd = FloatField('total_funding_usd', validators=[DataRequired()])
    organization_description = StringField('organization_description', validators=[DataRequired()])
    people_description = StringField('people_description', validators=[DataRequired()])
    status = SelectField('status', choices=[], validate_choice=True)
    category_list = SelectField('category_list', choices=[], validate_choice=True)
    category_groups_list = SelectField('category_groups_list', choices=[], validate_choice=True)
    primary_role = SelectField('primary_role', choices=['company', 'investor', 'school'], validate_choice=True)
    gender = SelectField('gender', choices=['Male', 'Female'], validate_choice=True)
    featured_job_title = SelectField('featured_job_title', choices=[], validate_choice=True)
    institution_name = SelectField('institution_name', choices=[], validate_choice=True)
    degree_type = SelectField('degree_type', choices=[], validate_choice=True)
    subject = SelectField('subject', choices=[], validate_choice=True)
    degree_is_completed = SelectField('degree_is_completed', choices=['True', 'False'], validate_choice=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method== 'GET':
        return render_template('home.html')
    else:
        data= CustomData(
            yrs_of_operation=request.form.get('yrs_of_operation'),
            yrs_since_last_funding=request.form.get('yrs_since_last_funding'),
            degree_length=request.form.get('degree_length'),
            per_exp_at_coy_start=request.form.get('per_exp_at_coy_start'),
            sponsor=request.form.get('sponsor'),
            speaker=request.form.get('speaker'),
            organizer=request.form.get('organizer'),
            exhibitor=request.form.get('exhibitor'),
            employee_count=request.form.get('employee_count'),
            total_funding_usd=request.form.get('total_funding_usd'),
            organization_description=request.form.get('organization_description'),
            people_description=request.form.get('people_description'),
            status=request.form.get('status'),
            category_list=request.form.get('category_list'),
            category_groups_list=request.form.get('category_groups_list'),
            primary_role=request.form.get('primary_role'),
            gender=request.form.get('gender'),
            featured_job_title=request.form.get('gender'),
            institution_name=request.form.get('gender'),
            degree_type=request.form.get('gender'),
            subject=request.form.get('subject'),
            degree_is_completed=request.form.get('degree_is_completed')







        )