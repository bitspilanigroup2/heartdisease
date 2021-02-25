
import configparser
import src.data.make_dataset as data
from .algo.logistic_regression import LogisticRegressionModel
from src.features.build_features import Encode
import pickle
import os

class Predict:
    def __init__(self):
        """[summary]
        """
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/tox.ini')
        self.model_path = config['data']['save-model'] + 'LogisticRegression.pkl'

    def predictModel(self):
        """[to predict the model]
        """
        print('Predicting Model')
        df = data.make_datasets()
        encode = Encode()
        df['X'] = encode.encodeColumns(df['X'])
        loaded_model = pickle.load(open(self.model_path, 'rb'))
        result = loaded_model.score(df['X'], df['Y'])
        print('Accuracy Score is ' + str(result))
        