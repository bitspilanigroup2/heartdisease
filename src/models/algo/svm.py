import configparser
import os
import pickle

from sklearn.svm import SVC


class SupportVectorMachineModel:

    def __init__(self):
        """[summary]
        """
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/tox.ini')
        self.save_path = config['data']['save-model'] + \
            'SupportVectorMachine.pkl'

    def build(self, data):
        lr = SVC()
        lr.fit(data['X'], data['Y'])
        with open(self.save_path, 'wb') as f:
            pickle.dump(lr, f)
