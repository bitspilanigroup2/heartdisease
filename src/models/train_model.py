
import src.data.make_dataset as data
from .algo.logistic_regression import LogisticRegressionModel
from src.features.build_features import Encode

class Train:
    def __init__(self):
        """[summary]
        """

    def trainModel(self):
        """[to train the model]
        """
        df = data.make_datasets()
        encode = Encode()
        df['X'] = encode.encodeColumns(df['X'])
        model = LogisticRegressionModel()
        model.build(df)
        