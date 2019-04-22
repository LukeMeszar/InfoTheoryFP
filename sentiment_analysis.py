import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import numpy as np
nltk.download('vader_lexicon')

def load_data(id):
    with open(id+'_codes_short.pkl', 'rb') as f:
        comments = pickle.load(f)
    comments = [x[0] for x in comments]
    return comments


def sentiment_analysis(comments):
    sid = SentimentIntensityAnalyzer()
    comments_with_sentiment = []
    for comment in comments:
        ss = sid.polarity_scores(comment)
        comments_with_sentiment.append((comment,ss['compound']))
    return comments_with_sentiment

def get_sentiment_counts(comments_with_sentiment):
    sentiment_counts = np.zeros(3)
    for comment in comments_with_sentiment:
        score = comment[1]
        if score > 0.25:
            sentiment_counts[0] += 1
        elif score < -0.25:
            sentiment_counts[2] += 1
        else:
            sentiment_counts[1] += 1
    sentiment_percentages = sentiment_counts/len(comments_with_sentiment)
    return sentiment_counts, sentiment_percentages



if __name__ == '__main__':
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    for id in id_list:
        print(id + ":")
        comments = load_data(id)
        comments_with_sentiment = sentiment_analysis(comments)
        sentiment_counts, sentiment_percentages = get_sentiment_counts(comments_with_sentiment)
        print("Counts:")
        print("Pos: ", sentiment_counts[0], "Neu: ", sentiment_counts[1], "Neg: ", sentiment_counts[2])
        print("Percentages:")
        print("Pos: ", sentiment_percentages[0], "Neu: ", sentiment_percentages[1], "Neg: ", sentiment_percentages[2])
