#!/usr/bin/env bash

# Author : hyunyoung2(hyun02.engineer@gmail.com)

"""
This module is for translating the test_set in similarity task on word2vec into Korean languages.
i.e. the test set is English version, to have Korean version of semantic task on words similarity, I
Translate them into Korean language for me and someone who want to do this job.
"""

import os
#import time # time sleep function
from googletrans import Translator

# Google test set file
ORIGINAL_FILE_NAME = "word-test.v1.normalized.txt"
OUT_FILE_NAME = "Korean_word_test.v1.txt"

IN_FILE = os.path.join("../../English/Efficient_Estimation_of_Word_Representations_in_Vector_Space", ORIGINAL_FILE_NAME)
OUT_FILE = os.path.join(os.getcwd(), OUT_FILE_NAME)
LINES = 0

def read_a_file(reader):
    """Read the file, word_test.v1.txt."""
    docs = [x for x in reader.readlines() if x != "\n"]
    return docs

def write_a_file(writer, docs):
    """write the resulting of reading word_test.v1.txt"""
    global LINES
    # Instannce of google's translatoer
    translator = Translator()

    for line_idx, line_val in enumerate(docs):
        if "//" in line_val:
            writer.write(line_val)
            print("Total Lines: {0}, partial lines: {1}, char: {2}".format(LINES, line_idx, line_val))
            LINES +=1
        elif ":" in line_val:
            writer.write(line_val)
            print("Total Lines: {0}, partial lines: {1}, char: {2}".format(LINES, line_idx, line_val))
            LINES +=1
        else:
            split_words = line_val.split()
            print("Total Lines: {0}, partial lines: {1}, char: {2}".format(LINES, line_idx, line_val))
            LINES +=1
            for word_idx, word_val in enumerate(split_words):
                print(word_val)
                translation = translator.translate(word_val, src='en', dest='ko')
                print(translation)
                if word_idx != 3:
                    writer.write(translation.text+"\t")
                else:
                    writer.write(translation.text+"\n")
                #time.sleep(5)

if __name__ == "__main__":
    print("start to translate.......")
    with open(IN_FILE, "r") as fr:
        TEMP = read_a_file(fr)
    # As you can see what they(Googletrans module) are saying,
    # This module use google tranlsate API,
    # But they don't guarantee stability that this module would work properly at all time.
    # Due to stability of this module, I split text into each set of 100 pairs.
    # In my case this works appropriately to my goal to translate my data.
    # 50 pair is the reason when you are with 100 pair. several response disappears. so I chnaged the 50 pairs
    SPLIT_LIST = list()
    for temp_idx, temp_val in enumerate(TEMP):
        if temp_idx == 0: # first subsete
            temp = list()
            temp.append(temp_val)
        elif temp_idx % 50 == 0 and temp_idx != 0:
            temp.append(temp_val)
            SPLIT_LIST.append(temp)
            temp = list()
        elif temp_idx == len(TEMP) -1: # last subset
            temp.append(temp_val)
            SPLIT_LIST.append(temp)
            del temp
        else:
            temp.append(temp_val)
    LINES = 0
    with open(OUT_FILE, "w") as fw:
        for split_list_idx, split_list_val in enumerate(SPLIT_LIST):
            write_a_file(fw, split_list_val)
    print("translation is done!!")
