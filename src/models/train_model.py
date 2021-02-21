
import src.data.make_dataset as data
from .algo.logistic_regression import LogisticRegressionModel

class Train:
    def __init__(self):
        """[summary]
        """

    def trainModel(self):
        """[to train the model]
        """
        df = data.make_datasets()
        model = LogisticRegressionModel()
        model.build(df)
        