import pickle
def load_data(id):
    with open(id+'_filtered.pkl', 'rb') as f:
        comments = pickle.load(f)
    return comments

def code_comments(comments, id):
    accepted_comment_counter = 0
    comment_codes = []
    for idx, comment in enumerate(comments):
        print("comments left: ", len(comments) - idx)
        if accepted_comment_counter > 40:
            print("Total comments accepted")
            break
        comment_code = [comment]
        print(comment)
        accept_reject = False
        accepted = False
        while not accept_reject:
            accept_reject_answer = input("accept comment y/n?")
            if accept_reject_answer == 'y':
                accepted = True
                accept_reject = True
                accepted_comment_counter += 1
            elif accept_reject_answer == 'n':
                accept_reject = True
        print(accepted_comment_counter)
        print("\n\n\n\n")
        if accepted:
            stance_chosen = False
            while not stance_chosen:
                stance_answer = input("Choose stance on NN: \n Options: \n 0: For NN, 1: Against NN, 2: Probably for NN, 3: \
                Probably against NN, 4: Ambigious}")
                if stance_answer in list(map(lambda x: str(x),list(range(5)))):
                    stance_chosen = True
                    comment_code.append(int(stance_answer))
            reason_chosen = False
            while not reason_chosen:
                reason_answer = input("Choose reason for stance: \n Options: \n 0: Political Reasons, 1: Economic Reasons, 2: Personal Reasons 3: Other")
                if reason_answer in list(map(lambda x: str(x),list(range(4)))):
                    reason_chosen = True
                    comment_code.append(int(reason_answer))

        comment_codes.append(tuple(comment_code))
        write_data(comment_codes, id)

def write_data(comment_codes, id):
    with open(id+'_codes.pkl', 'wb') as f:
        pickle.dump(comment_codes, f)

if __name__ == '__main__':
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    comments = load_data(id_list[4])
    code_comments(comments, id_list[4])
