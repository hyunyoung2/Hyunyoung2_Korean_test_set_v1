#!/usr/bin/env bash

# Author : hyunyoung2(hyun02.engineer@gmail.com)

"""
This module is for translating the test_set in similarity task on word2vec into Korean languages.
i.e. the test set is English version, to have Korean version of semantic task on words similarity, I
Translate them into Korean language for me and someone who want to do this job.
"""

import os
from googletrans import Translator

# Google test set file
ORIGINAL_FILE_NAME = ["word_relationship.answers", "word_relationship.questions"]
OUT_FILE_NAME = ["Korean_word_relationship.answers", "Korean_word_relationship.questions"]

IN_FILE_1 = os.path.join("../../English/Linguistic_Regularities_in_Continuous_Space_Word_Representations", ORIGINAL_FILE_NAME[1])
IN_FILE_0 = os.path.join("../../English/Linguistic_Regularities_in_Continuous_Space_Word_Representations", ORIGINAL_FILE_NAME[0])
OUT_FILE_1 = os.path.join(os.getcwd(), OUT_FILE_NAME[1])
OUT_FILE_0 = os.path.join(os.getcwd(), OUT_FILE_NAME[0])

def read_a_file(reader):
    """Read the file, word_test.v1.txt."""
    docs = [x for x in reader.readlines() if x != "\n"]
    return docs

def write_a_file(writer, docs):
    """write the resulting translation of word_relationship.questions"""
    # Instannce of google's translatoer
    translator = Translator()

    for line_idx, line_val in enumerate(docs):
        if "//" in line_val:
            writer.write(line_val)
        elif ":" in line_val:
            writer.write(line_val)
        else:
            split_words = line_val.split()
            print(line_idx)
            for word_idx, word_val in enumerate(split_words):
                print(word_val)
                translation = translator.translate(word_val, src='en', dest='ko')
                print(translation)
                if word_idx != 2:
                    writer.write(translation.text+"\t")
                else:
                    writer.write(translation.text+"\n")

def write_a_file_with_out_file_0(writer, docs):
    """write the resulting translation of word_relationship.questions"""
    # Instannce of google's translatoer
    translator = Translator()
   
    for line_idx, line_val in enumerate(docs):
        split_words = line_val.split()
        print(line_idx)
        for word_idx, word_val in enumerate(split_words):
            print(word_val)
            if word_idx == 0: 
                writer.write(word_val+"\t")
            else: 
                translation = translator.translate(word_val, src='en', dest='ko')
                print(translation)
                writer.write(translation.text+"\n")


def split_list(temp_list):
    """split function turning the list into each 100
    # As you can see what they(Googletrans module) are saying,
    # This module use google tranlsate API,
    # But they don't guarantee stability that this module would work properly at all time.
    # Due to stability of this module, I split text into each set of 100 pairs.
    # In my case this works appropriately to my goal to translate my data.
    # 50 pair is the reason when you are with 100 pair. several response disappears. so I chnaged the 50 pairs
    """
    split_list = list()
    for temp_idx, temp_val in enumerate(temp_list):
        if temp_idx == 0: # first subsete
            temp = list()
            temp.append(temp_val)
        elif temp_idx % 50 == 0 and temp_idx != 0:
            split_list.append(temp)
            temp = list()
        elif temp_idx == len(temp_list) -1: # last subset
            temp.append(temp_val)
            split_list.append(temp)
            del temp
        else:
            temp.append(temp_val)
    print(len(split_list))
    return split_list


if __name__ == "__main__":
    print("start to translate.......")
    with open(IN_FILE_1, "r") as fr:
        TEMP = read_a_file(fr)
    print("Temp 1",  len(TEMP))
    input("doesn't it right?")
    SPLIT_LIST = split_list(TEMP)

    print(SPLIT_LIST[0], len(SPLIT_LIST[0]), len(SPLIT_LIST))
    input("doesn't right")
    with open(OUT_FILE_1, "w") as fw:
        for split_list_idx, split_list_val in enumerate(SPLIT_LIST):
            write_a_file(fw, split_list_val)

    with open(IN_FILE_0, "r") as fr:
        TEMP = read_a_file(fr)
    print("Temp 0",  len(TEMP))
    SPLIT_LIST = split_list(TEMP)
    
    print(SPLIT_LIST[0], len(SPLIT_LIST[0]), len(SPLIT_LIST))
    with open(OUT_FILE_0, "w") as fw:
        for split_list_idx, split_list_val in enumerate(SPLIT_LIST):
           write_a_file_with_out_file_0(fw, split_list_val)

    print("translation is done!!")



