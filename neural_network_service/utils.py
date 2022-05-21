from nltk import BigramTagger as bt
from nltk import UnigramTagger as ut
from nltk.corpus import cess_esp as cess
from nltk.corpus import stopwords
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('cess_esp')
nltk.download('averaged_perceptron_tagger')


categories = [-1, 0, 1]


def get_class_tupple(input):
    classT = 'NEG'
    return (input, classT)


def create_word_embedding(add_pos_tags=True):
    comments = ['hello, how are you?', 'whats your name?']
    count = 0
    word_embedding = {}
    encoded_comments = []

    for comment in comments:
        # Segment sentence(s) to a list: [ "this", "is", "a", "sentence", "." ]
        # Normalize comment by converting to lowercase, for later mapping
        comment = nltk.word_tokenize(comment.lower())

        # Create a POS sentence: [ "word", "POS_tag", "word", "POS_tag", ... ]
        if add_pos_tags:
            comment = [ele for word_tuple in nltk.pos_tag(
                comment) for ele in word_tuple]

        print(comment)

        # Creating mapping: { "this": 1, "is": 2, ... } & encode each comment
        encoded_comment = []
        for word in comment:
            if word not in word_embedding:
                word_embedding[word] = count
                count += 1
            encoded_comment.append(word_embedding[word])
        encoded_comments.append(encoded_comment)

    print(encoded_comments)


def load_encoded_data(comments, data_split=0.8):
    '''
    :param comments: List of lists containing all comments
    :param categories: List containing labeled categories for associated comments
    :param data_split: The ratio of training to testing data (typical 80/20 split)
    :return x_train: Numpy array of encoded training sample(s) (comment)
    :return x_test: Numpy array of encoded testing sample(s) (comment)
    :return y_train: Numpy array of encoded training label (category)
    :return y_test: Numpy array of encoded testing label (category)
    '''

    # Word + Punctuation + POS Tags embedding
    encoded_comments = create_word_embedding(comments, add_pos_tags=True)

    # Word embedding, ensure you don't add the POS tags
    encoded_categories = create_word_embedding(categories, add_pos_tags=False)

    # Determine the training sample split point
    training_sample = int(len(encoded_comments) * data_split)

    # Split the dataset into training vs testing datasets
    x_train = np.array(encoded_comments[:training_sample])
    x_test = np.array(encoded_comments[training_sample:])
    y_train = np.array(encoded_categories[:training_sample])
    y_test = np.array(encoded_categories[training_sample:])

    return x_train, x_test, y_train, y_test
