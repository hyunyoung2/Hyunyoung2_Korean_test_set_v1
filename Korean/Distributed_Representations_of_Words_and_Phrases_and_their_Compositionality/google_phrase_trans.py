#!/usr/bin/env bash

# Author : hyunyoung2(hyun02.engineer@gmail.com)

"""
This module is for translating the test_set in similarity task on word2vec into Korean languages.
i.e. the test set is English version, to have Korean version of semantic task on words similarity, I
Translate them into Korean language for me and someone who want to do this job.
This file is for getting what kind of phrase is used for verification of word2vec performance.
"""

import os
from googletrans import Translator

# Google test set file
ORIGINAL_FILE_NAME = "questions-phrases.txt"
OUT_FILE_NAME = "Korean_questions-phrases.txt"

IN_FILE = os.path.join("../../English/Distributed_Representations_of_Words_and_Phrases_and_their_Compositionality", ORIGINAL_FILE_NAME)
OUT_FILE = os.path.join(os.getcwd(), OUT_FILE_NAME)


def read_a_file(reader):
    """Read the file, questions-words.txt."""
    docs = [x for x in reader.readlines() if x != "\n"]
    return docs

def write_a_file(writer, docs):
    """write those types of word phrase"""
    # Instannce of google's translatoer
    translator = Translator()

    for line_idx, line_val in enumerate(docs):
        if "//" in line_val:
            writer.write(line_val)
        elif ":" in line_val:
            writer.write(line_val)
        else:
            continue
            split_words = line_val.split()
            print(line_idx)
            for word_idx, word_val in enumerate(split_words):
                print(word_val)
                translation = translator.translate(word_val, src='en', dest='ko')
                print(translation)
                if word_idx != 3:
                    writer.write(translation.text+"\t")
                else:
                    writer.write(translation.text+"\n")

if __name__ == "__main__":
    print("start to translate.......")
    with open(IN_FILE, "r") as fr:
        TEMP = read_a_file(fr)
    # As you can see what they(Googletrans module) are saying,
    # This module use google tranlsate API,
    # But they don't guarantee stability that this module would work properly at all time.
    # Due to stability of this module, I split text into each set of 100 pairs.
    # In my case this works appropriately to my goal to translate my data.
    SPLIT_LIST = list()
    for temp_idx, temp_val in enumerate(TEMP):
        if temp_idx == 0: # first subsete
            temp = list()
            temp.append(temp_val)
        elif temp_idx % 100 == 0 and temp_idx != 0:
            SPLIT_LIST.append(temp)
            temp = list()
        elif temp_idx == len(TEMP) -1: # last subset
            temp.append(temp_val)
            SPLIT_LIST.append(temp)
            del temp
        else:
            temp.append(temp_val)

    with open(OUT_FILE, "w") as fw:
        for split_list_idx, split_list_val in enumerate(SPLIT_LIST):
            write_a_file(fw, split_list_val)
    print("translation is done!!")
