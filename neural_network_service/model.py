import time


class Model:
    def __init__(self) -> None:
        self.model = 'Modelo neuronal'
        self.trainModel()

    def trainModel(self):
        print('Training model...')
        time.sleep(5)
        print('Finished training model')

    def classify(self, input):
        print('Begin classification')
