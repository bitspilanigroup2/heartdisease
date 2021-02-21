# -*- coding: utf-8 -*-
import configparser
import os
import pandas as pd


def make_datasets():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/tox.ini')
    df = pd.read_csv(config['data']['train-dataset-path'])
    data = dict()
    input_columns = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'BMI', 'heartRate', 'glucose']
    input_columns = ['age','currentSmoker']
    output_column = 'TenYearCHD'
    data['X'] = df[input_columns]
    data['Y'] = df[output_column]
    return data
