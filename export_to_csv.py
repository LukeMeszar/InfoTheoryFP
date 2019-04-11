import pickle
import csv

def load_data(id):
    with open(id+'_filtered.pkl', 'rb') as f:
        comments = pickle.load(f)
    return comments


def write_to_csv(id, comments):
    with open(id+'.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        print(type(comments))
        wr.writerow(comments)

if __name__ == '__main__':
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    for id in id_list[:1]:
        comments = load_data(id)
        write_to_csv(id, comments)
