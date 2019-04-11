import pickle
def load_data(id):
    with open(id+'.pkl', 'rb') as f:
        comments = pickle.load(f)
    return comments

def accept_comments(comments):
    nn_dictionary = ['net neutraility', 'net', 'neutrality', 'neutral' 'nn', \
    'internet', 'comcast', 'isp', 'isps', 'internet service provider', 'ajit', 'pai', \
    'ftc', 'free market', 'free markets', 'market', 'markets', 'government', \
    'governments','regulation', 'regulations', 'at&t', 'throttle', 'throttling', \
    'traffic', 'freedom of speech', 'monopoly', 'monopolies', 'monopolistic', \
    'bandwidth', 'internet speed', 'internet speeds', 'verizon', 'premium browsing']
    accepted_comments = [False]*len(comments)
    for i,comment in enumerate(comments):
        split_comment = comment.split(' ')
        lower_split = [x.lower() for x in split_comment]
        for word in nn_dictionary:
            if word in lower_split:
                accepted_comments[i] = True
                break
    return accepted_comments

def filter_comments(comments, accepted_comments):
    filtered_comments = []
    for comment, status in zip(comments, accepted_comments):
        if status:
            filtered_comments.append(comment)
    return filtered_comments

def save_comments(comments, id):
    with open(id+'_filtered.pkl', 'wb') as f:
        pickle.dump(comments, f)


if __name__ == '__main__':
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    for id in id_list:
        comments = load_data(id)
        accepted_comments = accept_comments(comments)
        filtered_comments = filter_comments(comments, accepted_comments)
        save_comments(filtered_comments, id)
