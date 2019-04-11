import praw
import pickle

def scrape_comments(id):
    submission = reddit.submission(id=id)
    submission.comments.replace_more(limit=None)
    return [x.body for x in submission.comments.list()]

def save_comments(comments, id):
    with open(id+'.pkl', 'wb') as f:
        pickle.dump(comments, f)

if __name__ == '__main__':
    reddit = praw.Reddit(client_id='-UZu4Rfp6XRe4A',
                         client_secret='nNpyWIS414TyslDwE0HwzwpNEjg',
                         user_agent='linux:infortheory.finalproject:v1.0.0 (by /u/LukeMSki)')
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    for id in id_list:
        save_comments(scrape_comments(id), id)
