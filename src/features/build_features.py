import pandas as pd
from sklearn import preprocessing
from src.shared.config import loadConfig


class Encode:

    def __init__(self):
        self.config = loadConfig()

    def encodeColumns(self, df):
        """[summary]
        """
        if self.config['process']['encodeColumns'] == 'yes':
            education = pd.get_dummies(df['education'], prefix="cp")
            frames = [df, education]
            df = pd.concat(frames, axis=1)
            df = df.drop(columns=['education'])
        return df
