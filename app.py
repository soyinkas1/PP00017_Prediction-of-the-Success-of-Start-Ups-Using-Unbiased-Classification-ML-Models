from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, UTC
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired

import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.config.configuration import ConfigurationManager
from src.entity.config_entity import DataTransformationConfig


app =  Flask(__name__)
Bootstrap = Bootstrap(app)
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY



config = ConfigurationManager()
predict_config = config.get_prediction_pipeline_config()
webform_config = config.get_webform_config()


class WebForm(FlaskForm):
    
    yrs_of_operation = IntegerField('Years of Operation',default=0 ,validators=[InputRequired()])
    yrs_since_last_funding = IntegerField('Number of Years Since Last Funding', default=0 ,validators=[InputRequired()])
    degree_length = IntegerField("Promoter's Degree Length (Years)", default=0 ,validators=[InputRequired()])
    per_exp_at_coy_start = IntegerField("Promoter's Years of Experience at Start of Company", default=0 ,validators=[InputRequired()])
    sponsor = IntegerField('Number of Events as a sponsor', default=0 ,validators=[InputRequired()])
    speaker = IntegerField('Number of Events as a speaker', default=0 ,validators=[InputRequired()])
    organizer = IntegerField('Number of Events as an organizer', default=0 ,validators=[InputRequired()])
    exhibitor = IntegerField('Number of Events as an exhibitor', default=0 ,validators=[InputRequired()])
    employee_count = IntegerField('Company Employee Count', default=1 ,validators=[InputRequired()])
    total_funding_usd = FloatField('Total Funding in USD', default=0.00 ,validators=[InputRequired()])
    organization_description = StringField("Organization's Description (text)", validators=[DataRequired()], 
                                          render_kw={"placeholder": "Give a short description of the company"})
    people_description = StringField("Promoter's description (text)", validators=[DataRequired()], 
                                          render_kw={"placeholder": "Give a short description of the promoter"})
    status = SelectField('status', choices=[('acquired', 'acquired'), ('operating', 'operating'), ('ipo', 'ipo'), ('closed','closed')], 
                         validate_choice=True)
    category_list = SelectField('Category', choices=list(zip(webform_config.category_list, 
                                                                  webform_config.category_list)), validate_choice=True)
    category_groups_list = SelectField('Category Group', choices=list(zip(webform_config.category_groups_list, 
                                                                                webform_config.category_groups_list)), validate_choice=True)
    primary_role = SelectField('Company Primary Role', choices=[('company', 'company'), ('investor', 'investor'), ('school', 'school')], 
                               validate_choice=True)
    gender = SelectField('Promoter Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validate_choice=True)
    featured_job_title = SelectField('Job Title', choices=list(zip(webform_config.featured_job_title_list, 
                                                                            webform_config.featured_job_title_list)), validate_choice=True)
    institution_name = SelectField("Promoter's Institution Name", choices=list(zip(webform_config.institution_name_list, 
                                                                        webform_config.institution_name_list)), validate_choice=True)
    degree_type = SelectField("Promoter's Degree Type", choices=list(zip(webform_config.degree_type_list, 
                                                              webform_config.degree_type_list)), validate_choice=True)
    subject = SelectField("Promoter's Degree subject", choices=list(zip(webform_config.subject_list, 
                                                      webform_config.subject_list)), validate_choice=True)
    degree_is_completed = SelectField('Degree is completed?', choices=[('Yes'), ('No')], validate_choice=True)
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
        # name = form.name.data
        # form.name.data = ''
        data = CustomData(
        yrs_of_operation = form.yrs_of_operation.data,
        yrs_since_last_funding = form.yrs_since_last_funding.data,
        degree_length = form.degree_length.data,
        per_exp_at_coy_start = form.per_exp_at_coy_start.data,
        sponsor = form.sponsor.data,
        speaker = form.speaker.data,
        organizer = form.organizer.data,
        exhibitor = form.exhibitor.data,
        employee_count = form.employee_count.data,
        total_funding_usd = form.total_funding_usd.data,
        organization_description = form.organization_description.data,
        people_description = form.people_description.data,
        status = form.status.data,
        category_list = form.category_list.data,
        category_groups_list = form.category_groups_list.data,
        primary_role = form.primary_role.data,
        gender = form.gender.data,
        featured_job_title = form.featured_job_title.data,
        institution_name = form.institution_name.data,
        degree_type = form.degree_type.data,
        subject = form.subject.data,
        degree_is_completed = form.degree_is_completed.data,
        
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        
     
        obj = PredictPipeline(config=predict_config)
        predict = obj.predict(pred_df)

        return render_template('results.html', predict=predict)
    
    else:

        return render_template('predictor.html', form=form)