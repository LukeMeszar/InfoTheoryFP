import praw

reddit = praw.Reddit(client_id='-UZu4Rfp6XRe4A',
                     client_secret='nNpyWIS414TyslDwE0HwzwpNEjg',
                     user_agent='linux:infortheory.finalproject:v1.0.0 (by /u/LukeMSki)')

# for submission in reddit.subreddit('learnpython').hot(limit=10):
#     print(submission.title)

# subreddit = reddit.subreddit('redditdev')
# print(subreddit.display_name)

submission = reddit.submission(id='b5e6u9')
submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)
#     print("\n\n\n")

all_comments = [x.body for x in submission.comments.list()]
# print(all_comments)
print(len(all_comments))
