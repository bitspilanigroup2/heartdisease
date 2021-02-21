from src.models.train_model import Train

class HeartDisease:

    def __init__(self):
        """[Class Initialization]
        """

    def trainModel(self):
        """[to train the model]
        """
        train = Train()
        train.trainModel()

if __name__ == '__main__':
    print('Starting Heart Disease Model Training')
    heartdisease = HeartDisease()
    heartdisease.trainModel()
    print('Ending Heart Disease Model Training')