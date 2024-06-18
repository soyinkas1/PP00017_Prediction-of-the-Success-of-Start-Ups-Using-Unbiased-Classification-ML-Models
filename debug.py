import pandas as pd

df = pd.read_csv('D:\\OneDrive\\Documents\\Personal Project Portfolio\\PP00017_Prediction of the Success of Start-Ups\\artifacts\\data_transformation\\train_data.csv', nrows=2, low_memory=False)

print(df.info())