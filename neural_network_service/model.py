import numpy as np
import pandas as pd
from tensorflow import keras
# x86_64
# from keras.utils import pad_sequences, to_categorical
# aarch64
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
####
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.layers import Dense, Dropout, Activation, Embedding, Conv1D, GlobalMaxPooling1D
from utils import load_encoded_data, parseInputs, flatten


class Model:
    max_words, batch_size, maxlen, epochs = 4220, 64, 70, 100
    embedding_dims, filters, kernel_size, hidden_dims = 20, 100, 5, 50

    # Generate split training and testing data (80% training, 20% testing)
    x_train, x_test, y_train, y_test = load_encoded_data(data_split=0.75)

    # Determine the number of categories + default(i.e. sentence types)
    num_classes = np.max(y_train) + 1

    # Vectorize the output sentence type classifcations to Keras readable format
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    # Pad the input vectors to ensure a consistent length
    x_train = pad_sequences(x_train, maxlen=maxlen, padding='post')
    x_test = pad_sequences(x_test, maxlen=maxlen, padding='post')

    early_stopping_monitor = EarlyStopping(
        monitor='val_loss',
        min_delta=0.001,
        patience=10,
        verbose=0,
        mode='min',
        restore_best_weights=True
    )
    mcp_save = ModelCheckpoint(
        './best_models/md.ep{epoch:02d}-loss{val_loss:.2f}-acc{val_accuracy:.2f}.hdf5',
        save_best_only=True,
        monitor='val_loss',
        mode='min'
    )
    reduce_lr_loss = ReduceLROnPlateau(
        monitor='val_loss', factor=0.1, patience=7, verbose=1, min_delta=0.0001, mode='min')

    # print(x_train)

    def __init__(self) -> None:
        self.model = Sequential()

        # Created Embedding (Input) Layer (max_words) --> Convolutional Layer
        self.model.add(
            Embedding(self.max_words, self.embedding_dims, input_length=self.maxlen))
        self.model.add(Dropout(0.2))  # masks various input values

        # Create the convolutional layer
        self.model.add(Conv1D(self.filters, self.kernel_size,
                       padding='valid', activation='relu', strides=1))

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

    def trainModel(self):
        cbs = [self.early_stopping_monitor, self.mcp_save, self.reduce_lr_loss]

        self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size,
                       epochs=self.epochs, validation_data=(self.x_test, self.y_test), callbacks=cbs)
        score = self.model.evaluate(
            self.x_test, self.y_test, batch_size=self.batch_size)
        prediction = self.model.predict(
            self.x_test, batch_size=self.batch_size)

        print(self.model.metrics_names)
        print(score)

        prob_neg = 0
        prob_pos = 0
        prob_net = 0
        for p in prediction:
            prob_net += p[0]
            prob_neg += p[1]
            prob_pos += p[2]

        prob_neg = prob_neg / len(prediction)
        prob_net = prob_net / len(prediction)
        prob_pos = prob_pos / len(prediction)

        print('prob neutral:', prob_net)
        print('prob negativa:', prob_neg)
        print('prob positiva:', prob_pos)

    def analyze_results(self, result_set, lucky=False):
        df = pd.DataFrame(result_set)
        df.columns = result_set[0].keys()
        inputs = flatten(df.values.tolist())

        parsedInputs = parseInputs(inputs)
        parsedInputs = pad_sequences(parsedInputs, maxlen=70, padding='post')
        if lucky == False:
            savedModel = keras.models.load_model(
                './best_models/POTENTIAL_MODEL.ep29-loss0.62-acc0.84.hdf5')
            savedPred = savedModel.predict(parsedInputs)
            print('Best model predictions: ', savedPred.argmax(axis=-1))
            for idx, phrase in enumerate(inputs):
                print(phrase)
                print(savedPred[idx].argmax(axis=-1))


if __name__ == '__main__':
    classifier = Model()
    x_predictions = parseInputs([
        "Este es un tweet de prueba",
        "Ese candidato es un paraco narcotraficante",
        "Excelentes noticias que buena persona",
        "malparido paraco no tiene ni idea de lo que le hace al pais, el y sus subditos",
        "ese canelo es un pesimo boxeador, no sabe nada del deporte",
        "que buenas noticias, te doy las gracias por eso",
        "Que buena persona eres, te felicito por tu labor y por tu dedicacion, te doy las gracias por tu excelente trabajo",
        "este es un tweet de prueba, ese candidato es un malparido porque no sabe que esta haciendo con el pais. Esta empeorando la situacion economica de todos los colombianos y tiene el descaro de decir que le va hacer bien al pais cuando todo lo que ha hecho ha sido pesimo y de mala calidad",
        "que hermosa persona eres, te quiero como amigo y te amo como hermano"
    ])

    x_predictions = pad_sequences(x_predictions, maxlen=70, padding='post')
    prediction = classifier.model.predict(x_predictions)

    savedModel = keras.models.load_model(
        './best_models/POTENTIAL_MODEL.ep29-loss0.62-acc0.84.hdf5')
    savedPred = savedModel.predict(x_predictions)

    print('New predictions', prediction.argmax(axis=-1))
    print('Saved model', savedPred.argmax(axis=-1))
