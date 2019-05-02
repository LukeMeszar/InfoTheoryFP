import pickle
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models
from gensim.test.utils import datapath
from gensim.test.utils import common_corpus, common_dictionary
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
import csv

def load_data(id):
    with open(id+'.pkl', 'rb') as f:
        comments = pickle.load(f)
    return comments

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

def process_thread(comments):
    processed_thread = []
    for comment in comments:
        processed_thread.append(preprocess(comment))
    return processed_thread

def create_dictionary(processed_thread):
    dictionary = gensim.corpora.Dictionary(processed_thread)
    dictionary.filter_extremes(no_below=2, no_above=0.5, keep_n=100000)
    return dictionary
def create_bow_corpus(dictionary, processed_thread):
    return [dictionary.doc2bow(comment) for comment in processed_thread]

def create_tfidf(bow_corpus):
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]
    return corpus_tfidf

def bow_model(bow_corpus, dictionary):
    lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)
    return lda_model

def tfidf_model(corpus_tfidf, dictionary):
    lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=5, id2word=dictionary, passes=2, workers=4)
    return lda_model_tfidf

def save_model(model, id):
    model.save('topic_models/model' + id)



if __name__ == '__main__':
    np.random.seed(2018)
    nltk.download('wordnet')
    stemmer = SnowballStemmer('english')
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    comments = []
    with open('/home/luke/TestCode/tech.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in readCSV:
            comments.append(row[0])
    processed_thread = process_thread(comments)
    dictionary = create_dictionary(processed_thread)
    bow_corpus = create_bow_corpus(dictionary, processed_thread)
    corpus_tfidf = create_tfidf(bow_corpus)
    #lda_model = bow_model(bow_corpus, dictionary)
    lda_model_tfidf = tfidf_model(corpus_tfidf, dictionary)
    for idx, topic in lda_model_tfidf.print_topics(-1):
        print('Topic: {} Word: {}'.format(idx, topic))
    #save_model(lda_model_tfidf, id_list[0])
    print(processed_thread[0])
    for index, score in sorted(lda_model_tfidf[bow_corpus[0]], key=lambda tup: -1*tup[1]):
        print("\nScore: {}\t \nTopic: {}".format(score, lda_model_tfidf.print_topic(index, 10)))
