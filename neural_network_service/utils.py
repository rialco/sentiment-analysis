import numpy as np
import nltk
import random
import pandas as pd
from dictionary import palabras_negativas, palabras_positivas, palabras_stop, puntuaciones
nltk.download('punkt')


def get_tweet_with_sentiment_pos(input):
    tweetTokens = nltk.word_tokenize(input, "spanish")
    cleanedTweet = []
    for word in tweetTokens:
        if len(word) == 1:
            continue
        if word.lower() in palabras_stop:
            continue
        if word.lower() in puntuaciones:
            continue
        if word.lower() in (string.lower() for string in palabras_positivas):
            cleanedTweet.append(word)
            cleanedTweet.append('POS')
            continue
        if word.lower() in (string.lower() for string in palabras_negativas):
            cleanedTweet.append(word)
            cleanedTweet.append('NEG')
            continue
        cleanedTweet.append(word)
        cleanedTweet.append('NET')
    return cleanedTweet


def create_word_embedding(phrases, add_pos_tags=False):
    count = 0
    word_embedding = {}
    encoded_phrases = []

    for phrase in phrases:
        cleanPhrase = [phrase]

        if add_pos_tags:
            cleanPhrase = get_tweet_with_sentiment_pos(phrase)

        encoded_phrase = []
        for word in cleanPhrase:
            if word not in word_embedding:
                word_embedding[word] = count
                count += 1
            encoded_phrase.append(word_embedding[word])
        encoded_phrases.append(encoded_phrase)
    return encoded_phrases


def load_encoded_data(data_split=0.8):
    data = pd.read_csv('./training.csv')
    # data = data.sample(frac=1).reset_index(drop=True)
    classified_tweets = data.values.tolist()

    random.shuffle(classified_tweets)

    tweets, categories = [], []
    for tweet, category in classified_tweets:
        tweets.append(tweet)
        categories.append(category)

    # Word + Punctuation + POS Tags embedding
    encoded_tweets = create_word_embedding(tweets, add_pos_tags=True)

    # Word embedding, ensure you don't add the POS tags
    encoded_categories = create_word_embedding(categories, add_pos_tags=False)

    # Determine the training sample split point
    training_sample = int(len(encoded_tweets) * data_split)

    # Split the dataset into training vs testing datasets
    x_train = np.array(encoded_tweets[:training_sample], dtype=object)
    x_test = np.array(encoded_tweets[training_sample:], dtype=object)
    y_train = np.array(encoded_categories[:training_sample], dtype=object)
    y_test = np.array(encoded_categories[training_sample:], dtype=object)
    return x_train, x_test, y_train, y_test


def parseInputs(inputs):
    encoded_input = create_word_embedding(inputs, add_pos_tags=True)
    return np.array(encoded_input, dtype=object)


def flatten(t):
    return [item for sublist in t for item in sublist]
