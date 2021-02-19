import src.models.train_model as train

class HeartDisease:

    def __init__(self):
        """[summary]
        """

    def trainModel(self):
        """[summary]
        """
        train.trainModel(self)

if __name__ == '__main__':
    print('Starting Heart Disease Model Training')
    heartdisease = HeartDisease()
    heartdisease.trainModel()
    print('Ending Heart Disease Model Training')