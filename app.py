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
from src.config.configuration import ConfigurationManager

app =  Flask(__name__)
Bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "kokoroasiri"


## Route for a home page

class WebForm(FlaskForm):
    config = ConfigurationManager()
    webform_config = config.get_webform_config()
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
    status = SelectField('status', choices=['acquired', 'operating', 'ipo', 'closed'], validate_choice=True)
    category_list = SelectField('category_list', choices=[webform_config.category_list], validate_choice=True)
    category_groups_list = SelectField('category_groups_list', choices=[webform_config.category_groups_list], validate_choice=True)
    primary_role = SelectField('primary_role', choices=['company', 'investor', 'school'], validate_choice=True)
    gender = SelectField('gender', choices=['Male', 'Female'], validate_choice=True)
    featured_job_title = SelectField('featured_job_title', choices=[webform_config.featured_job_title_list], validate_choice=True)
    institution_name = SelectField('institution_name', choices=[webform_config.institution_name_list], validate_choice=True)
    degree_type = SelectField('degree_type', choices=[webform_config.degree_type_list], validate_choice=True)
    subject = SelectField('subject', choices=[webform_config.subject_list], validate_choice=True)
    degree_is_completed = SelectField('degree_is_completed', choices=['True', 'False'], validate_choice=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
        # name = form.name.data
        # form.name.data = ''
        yrs_of_operation = form.yrs_of_operation.data
        yrs_since_last_funding = form.yrs_since_last_funding.data
        per_exp_at_coy_start = form.per_exp_at_coy_start.data
        sponsor = form.sponsor.data
        speaker = form.speaker.data
        organizer = form.organizer.data
        exhibitor = form.exhibitor.data
        employee_count = form.employee_count.data
        total_funding_usd = form.total_funding_usd.data
        organization_description = form.organization_description.data
        people_description = form.people_description.data
        status = form.status.data
        category_list = form.category_list.data
        category_groups_list = form.category_groups_list.data
        primary_role = form.primary_role.data
        gender = form.gender.data
        featured_job_title = form.featured_job_title.data
        institution_name = form.institution_name.data
        degree_type = form.degree_type.data
        subject = form.subject.data
        degree_is_completed = form.degree_is_completed.data
    return render_template('predictor.html', form=form)