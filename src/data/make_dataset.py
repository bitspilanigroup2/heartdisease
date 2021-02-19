# -*- coding: utf-8 -*-
from pathlib import Path
import configparser
import os
import pandas as pd



def make_datasets():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/tox.ini')
    data = pd.read_csv(config['data']['train-dataset-path'])
    print(data.head())
    print(data.shape)