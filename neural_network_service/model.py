import numpy as np
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding, Conv1D, GlobalMaxPooling1D


class Model:
    max_words, batch_size, maxlen, epochs = 10000, 64, 500, 2
    embedding_dims, filters, kernel_size, hidden_dims = 50, 250, 5, 150

    # Generate split training and testing data (80% training, 20% testing)
    x_train, x_test, y_train, y_test = load_encoded_data(data_split=0.8)

    # Determine the number of categories + default(i.e. sentence types)
    num_classes = np.max(y_train) + 1

    # Vectorize the output sentence type classifcations to Keras readable format
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    # Pad the input vectors to ensure a consistent length
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

    def __init__(self) -> None:
        self.model = Sequential()
        # Created Embedding (Input) Layer (max_words) --> Convolutional Layer
        self.model.add(
            Embedding(self.max_words, self.embedding_dims, input_length=self.maxlen))
        self.model.add(Dropout(0.2))  # masks various input values

        # Create the convolutional layer
        self.model.add(Conv1D(self.filters, self.kernel_size, padding='valid',
                              activation='relu', strides=1))

        # Create the pooling layer
        self.model.add(GlobalMaxPooling1D())

        # Create the fully connected layer
        self.model.add(Dense(self.hidden_dims))
        self.model.add(Dropout(0.2))
        self.model.add(Activation('relu'))

        # Create the output layer (num_classes)
        self.model.add(Dense(self.num_classes))
        self.model.add(Activation('softmax'))

        # Add optimization method, loss function and optimization value
        self.model.compile(loss='categorical_crossentropy',
                           optimizer='adam', metrics=['accuracy'])
        self.trainModel()

    def trainModel(self):
        print('Training model...')
        # "Fit the model" (train model), using training data (80% of datset)
        self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size,
                       epochs=self.epochs, validation_data=(self.x_test, self.y_test))
        print('Finished training model')

    def classify(self, input):
        print('Begin classification')
        return self.model.call(input, training=False)
