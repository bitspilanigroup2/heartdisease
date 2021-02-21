import configparser
import os
import pandas as pd
from sklearn import preprocessing


class Encode:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/tox.ini')

    def encodeColumns(self,df):
        """[summary]
        """
        education = pd.get_dummies(df['education'], prefix = "cp")
        frames = [df, education]
        df = pd.concat(frames, axis = 1)
        df = df.drop(columns = ['education'])
        return df