import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer
from src.shared.config import loadConfig


def imputeByMean(data, nonNumeric):
    # for median imputation replace 'mean' with 'median'
    imputedMean = SimpleImputer(strategy='mean')
    dataNumeric = data.drop(nonNumeric, axis=1)
    imputedMean.fit(dataNumeric)
    imputedData = imputedMean.transform(dataNumeric)

    d1 = pd.DataFrame(imputedData)
    d1.columns = dataNumeric.columns
    finalImputedData = pd.concat([d1, data.loc[:, nonNumeric]], axis=1)
    ## imputedData.columns = data.columns
    return finalImputedData


def make_datasets(mode):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    config = loadConfig()
    path = os.getcwd() + config['data'][mode]
    print("printinggggg...." +path)
    df = pd.read_csv(path)
    cols = df.columns
    num_cols = df._get_numeric_data().columns
    nonNumeric = list(set(cols) - set(num_cols))
    df = imputeByMean(df, nonNumeric)
    df[['education', 'cigsPerDay', 'BPMeds', 'totChol', 'sysBP', 'diaBP', 'BMI', 'glucose']] = df[[
        'education', 'cigsPerDay', 'BPMeds', 'totChol', 'sysBP', 'diaBP', 'BMI', 'glucose']].astype(int)
    df["education"].replace(np.nan, df["education"].astype(
        "float32").mean(axis=0), inplace=True)
    df["cigsPerDay"].replace(np.nan, df["cigsPerDay"].astype(
        "float32").mean(axis=0), inplace=True)
    df["BPMeds"].replace(np.nan, df["BPMeds"].astype(
        "float32").mean(axis=0), inplace=True)
    df["totChol"].replace(np.nan, df["totChol"].astype(
        "float32").mean(axis=0), inplace=True)
    df["BMI"].replace(np.nan, df["BMI"].astype(
        "float32").mean(axis=0), inplace=True)
    df["glucose"].replace(np.nan, df["glucose"].astype(
        "float32").mean(axis=0), inplace=True)
    data = dict()
    input_columns = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
                     'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
                     'diaBP', 'BMI', 'heartRate', 'glucose']
    output_column = 'TenYearCHD'
    data['X'] = df[input_columns]
    data['Y'] = df[output_column]
    return data
