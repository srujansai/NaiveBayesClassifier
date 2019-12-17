from queue import Queue
import math
import os
import collections
import json


pos_term_dict = {}
neg_term_dict = {}
final_vocab_dict = {}

dict_list = []

def form_vocab(training_dir, model_file):

    pos_dir_path = training_dir + '/pos'
    neg_dir_path = training_dir + '/neg'
    for name in sorted(os.listdir(pos_dir_path)):
        with open(pos_dir_path + '\\' + name) as f:
            words = f.read().split()

        for word in words:

            if not (final_vocab_dict.__contains__(word)):
                final_vocab_dict[word] = 1
            else:
                final_vocab_dict[word] += 1

            if not (pos_term_dict.__contains__(word)):
                pos_term_dict[word] = 1
            else:
                pos_term_dict[word] += 1

    for name in sorted(os.listdir(neg_dir_path)):
        with open(neg_dir_path + '\\' + name) as f:
            words = f.read().split()

        for word in words:

            if not (final_vocab_dict.__contains__(word)):
                final_vocab_dict[word] = 1
            else:
                final_vocab_dict[word] += 1

            if not (neg_term_dict.__contains__(word)):
                neg_term_dict[word] = 1
            else:
                neg_term_dict[word] += 1



    for word in final_vocab_dict:
        if final_vocab_dict[word] < 5:
            if pos_term_dict.__contains__(word):
                pos_term_dict.pop(word)
            if neg_term_dict.__contains__(word):
                neg_term_dict.pop(word)





    output_file = open(model_file, "w")
    dict_list = [final_vocab_dict, pos_term_dict, neg_term_dict]
    json.dump(dict_list, output_file, ensure_ascii=True, indent=5)
    output_file.close()



a = input('Enter the directory of the training data : ')

b = input('Enter the output model file: ')

form_vocab(a,b)



