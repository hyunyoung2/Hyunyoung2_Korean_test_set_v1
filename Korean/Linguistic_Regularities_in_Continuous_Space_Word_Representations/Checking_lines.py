#!/usr/bin/env bash 

# Author : hyunyoung2

import os

INFILE=os.path.join("../../English/Linguistic_Regularities_in_Continuous_Space_Word_Representations","word_relationship.questions")

def read_a_file(path):
    temp = [x for x in path.readlines() if x != "\n"]
    print("the length of docs' lines: {}".format(len(temp)))

if __name__ == "__main__":
    with open(INFILE, "r") as rf:
        read_a_file(rf)
    
