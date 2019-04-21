import pickle
import itertools as it
import numpy as np

def load_data(id):
    with open(id+'_codes_short.pkl', 'rb') as f:
        comments = pickle.load(f)
    return comments

def write_data(comment_codes, id):
    with open(id+'_codes_short.pkl', 'wb') as f:
        pickle.dump(comment_codes, f)

# def remove_discarded_comments(id):
#     comments = load_data(id)
#     actual_comments = []
#     for comment in comments:
#         if len(comment) == 3:
#             actual_comments.append(comment)
#     write_data(actual_comments, id)



def get_counts_for_codes(id,num_stance_codes, num_reason_codes):
    cartesian_product_counts = np.zeros((num_stance_codes, num_reason_codes))
    stance_counts = np.zeros(num_stance_codes)
    reason_counts = np.zeros(num_reason_codes)
    coded_data = load_data(id)
    for comment in coded_data:
        coded_stance, coded_reason = comment[1], comment[2]
        cartesian_product_counts[coded_stance, coded_reason] += 1
    for i in np.arange(num_stance_codes):
        stance_counts[i] = np.sum(cartesian_product_counts[i,:])
    for i in np.arange(num_reason_codes):
        reason_counts[i] = np.sum(cartesian_product_counts[:,i])
    return cartesian_product_counts, stance_counts, reason_counts

def get_percentages(cartesian_product_counts,stance_counts,reason_counts):
    total_comments = np.sum(cartesian_product_counts)
    cartesian_product_percentages = np.zeros_like(cartesian_product_counts)
    stance_percentages = np.zeros_like(stance_counts)
    reason_percentages = np.zeros_like(reason_counts)
    for i in np.arange(len(stance_counts)):
        stance_percentages[i] = stance_counts[i]/total_comments
    for i in np.arange(len(reason_counts)):
        reason_percentages[i] = reason_counts[i]/total_comments
    c_product_shape = cartesian_product_counts.shape
    for i,j in it.product(np.arange(c_product_shape[0]), np.arange(c_product_shape[1])):
        cartesian_product_percentages[i,j] = cartesian_product_counts[i,j]/total_comments
    return cartesian_product_percentages, stance_percentages, reason_percentages

def write_percentages(id, cartesian_product_percentages, stance_percentages, reason_percentages):
    stance_prints = ['Stances:']
    for idx in np.argsort(stance_percentages)[::-1]:
        out = 'Percentage for ' + codebook_stance[idx] + ': ' + str(stance_percentages[idx])
        stance_prints.append(out)
    with open(id+'_percentages.txt', 'w') as f:
        for item in stance_prints:
            f.write(item+"\n")
    reason_prints = ['Reasons:']
    for idx in np.argsort(reason_percentages)[::-1]:
        out = 'Percentage for ' + codebook_reason[idx] + ': ' + str(reason_percentages[idx])
        reason_prints.append(out)
    with open(id+'_percentages.txt', 'a') as f:
        for item in reason_prints:
            f.write(item+"\n")
    product_prints = ['Combined Stance and Reason:']
    c_product_shape = cartesian_product_counts.shape
    for i,j in it.product(np.arange(c_product_shape[0]), np.arange(c_product_shape[1])):
        pass 


if __name__ == '__main__':
    id_list = ['7ei3b1', '7en6do', 'adt1a3', '7gzh5a', '6ivklm']
    codebook_stance = {0: "For NN", 1: "Against NN", 2: "Probably for NN", 3: \
    "Probably against NN", 4: "Ambigious"}
    codebook_reason = {0: "Political Reasons", 1: "Economic Reasons", 2: "Personal Reasons", 3: "Other"}
    cartesian_product_counts, stance_counts, reason_counts = get_counts_for_codes(id_list[0], 5,4)
    # print(cartesian_product_counts, stance_counts, reason_counts)
    #print(np.sum(cartesian_product_counts), np.sum(stance_counts), np.sum(reason_counts))
    cartesian_product_percentages, stance_percentages, reason_percentages = \
     get_percentages(cartesian_product_counts,stance_counts,reason_counts)
    # print(cartesian_product_percentages, stance_percentages, reason_percentages)
    write_percentages(id_list[0], cartesian_product_percentages, stance_percentages, reason_percentages)
