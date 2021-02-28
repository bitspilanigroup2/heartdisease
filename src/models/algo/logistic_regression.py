import configparser
import os
import pickle
from src.shared.constants import CONFIG_PATH
from sklearn.linear_model import LogisticRegression


class LogisticRegressionModel:

    def __init__(self):
        """[summary]
        """
        config = configparser.ConfigParser()
        config.read(os.getcwd() + CONFIG_PATH, encoding="utf-8")
        #config.read(CONFIG_PATH, encoding="utf-8")
        self.save_path = os.getcwd() + config['data']['save-model'] + \
            'LogisticRegression.pkl'

    def build(self, data):
        lr = LogisticRegression(max_iter=10000)
        lr.fit(data['X'], data['Y'])
        with open(self.save_path, 'wb') as f:
            pickle.dump(lr, f)
