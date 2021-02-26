import fire

from src.models.predict_model import Predict
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
        predict = Predict()
        predict.predictModel()


if __name__ == '__main__':
    heartdisease = HeartDisease()
    fire.Fire(heartdisease)
