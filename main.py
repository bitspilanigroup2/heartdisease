from src.models.train_model import Train
from src.models.predict_model import Predict

class HeartDisease:

    def __init__(self):
        """[Class Initialization]
        """

    def trainModel(self):
        """[to train the model]
        """
        train = Train()
        train.trainModel()

    def predictModel(self):
        """[to train the model]
        """
        predict = Predict()
        predict.predictModel()

if __name__ == '__main__':
    heartdisease = HeartDisease()
    # heartdisease.trainModel()
    heartdisease.predictModel()