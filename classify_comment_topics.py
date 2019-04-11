import gensim
from gensim import corpora, models
from gensim.test.utils import datapath
from gensim.test.utils import common_corpus, common_dictionary

def load_model(id):
    model = gensim.models.LdaMulticore.load('topic_models/model' + id)
    return model

def user_choose_topics(model):
    acceptable_topic_list = [True]*len(model.print_topics(-1))
    print(acceptable_topic_list)
    for idx, topic in model.print_topics(-1):
        print('Topic: {} Word: {}'.format(idx, topic))
        answer = input('accept topic? y/n')
        if answer == 'n':
            acceptable_topic_list[idx] = False
    print(acceptable_topic_list)



if __name__ == '__main__':
    print("main")
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    model = load_model(id_list[0])
    user_choose_topics(model)
