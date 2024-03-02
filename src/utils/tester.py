import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import lightgbm as lgb

yaml_content = """
models:
  Logistic Regression: LogisticRegression()
  SVM: SVC()
  Random Forest: RandomForestClassifier()
  XGB: XGBClassifier()
  LightGBM: lgb.LGBMClassifier()
"""

# Parse YAML content
parsed_content = yaml.safe_load(yaml_content)

# Convert string representations to actual objects
models = {}
for model_name, model_object in parsed_content['models'].items():
    print(model_object)
    models[model_name] = eval(model_object)

# Testing the models
for model_name, model in models.items():
    print(f"Model: {model_name}")
    print(model)