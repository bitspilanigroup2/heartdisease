import fire

import src.models.predict_model as predictor
from src.models.train_model import Train


class HeartDisease:

    def __init__(self):
        """[Class Initialization]
        """

    def trainModel(self):
        """[to train the model which includes multiple algorithms like Logistic Regression, SVM]
        """
        train = Train()
        train.trainModel()

    def predictModel(self):
        """[to predict the model]
        """
        predictor.Predict()


if __name__ == '__main__':
    heartdisease = HeartDisease()
    fire.Fire(heartdisease)
