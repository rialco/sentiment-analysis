from gc import callbacks
import numpy as np
import keras
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers import Dense, Dropout, Activation, Embedding, Conv1D, GlobalMaxPooling1D
from utils import load_encoded_data, parseInputs


class Model:
    max_words, batch_size, maxlen, epochs = 2400, 64, 50, 50
    embedding_dims, filters, kernel_size, hidden_dims = 12, 60, 2, 30

    # Generate split training and testing data (80% training, 20% testing)
    x_train, x_test, y_train, y_test = load_encoded_data(data_split=0.8)

    # Determine the number of categories + default(i.e. sentence types)
    num_classes = np.max(y_train) + 1

    # Vectorize the output sentence type classifcations to Keras readable format
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    # Pad the input vectors to ensure a consistent length
    x_train = pad_sequences(x_train, maxlen=maxlen, padding='post')
    x_test = pad_sequences(x_test, maxlen=maxlen, padding='post')

    print(x_train)

    def __init__(self) -> None:
        self.model = Sequential()

        # Created Embedding (Input) Layer (max_words) --> Convolutional Layer
        self.model.add(Embedding(self.max_words, self.embedding_dims, input_length=self.maxlen))
        self.model.add(Dropout(0.2)) # masks various input values
            
        # Create the convolutional layer
        self.model.add(Conv1D(self.filters, self.kernel_size, padding='valid', activation='relu', strides=1))

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
        early_stopping_monitor = EarlyStopping(
            monitor='val_loss',
            min_delta=0,
            patience=50,
            verbose=0,
            mode='min',
            restore_best_weights = True
        )
        mcp_save = ModelCheckpoint('.mdl_wts.hdf5', save_best_only=True, monitor='val_loss', mode='min')
        reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.001, patience=10, verbose=1, min_delta=0, mode='min')
        print('Training model...')
        # "Fit the model" (train model), using training data (80% of datset)
        self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size,
                       epochs=self.epochs, validation_data=(self.x_test, self.y_test), callbacks=[mcp_save, reduce_lr_loss])
        print('Finished training model')
        score = self.model.evaluate(self.x_test, self.y_test, batch_size=self.batch_size)
        print(self.model.metrics_names)
        print(score)

if __name__ == '__main__':
    classifier = Model()
    x_predictions = parseInputs([
    'psa Este es un tweet de prueba',
    'Ese candidato es un paraco narcotraficante', 
    'Excelentes noticias que buena persona',
    'malparido paraco no tiene ni idea de lo que le hace al pais, el y sus subditos',
    'ese canelo es un pesimo boxeador, no sabe nada del deporte', 
    'que buenas noticias, te doy las gracias por eso',
    'Que buena persona eres, te felicito por tu labor y por tu dedicacion, te doy las gracias por tu excelente trabajo',
    'este es un tweet de prueba, ese candidato es un malparido porque no sabe que esta haciendo con el pais. Esta empeorando la situacion economica de todos los colombianos y tiene el descaro de decir que le va hacer bien al pais cuando todo lo que ha hecho ha sido pesimo y de mala calidad'
    ])
    x_predictions = pad_sequences(x_predictions, maxlen=50, padding='post')
    prediction = classifier.model.predict(x_predictions)
    print(prediction.argmax(axis=-1))
