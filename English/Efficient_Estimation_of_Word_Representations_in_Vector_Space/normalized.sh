#!/usr/bin/env bash

# Author : hyunyoung2 

IN_FILE="word-test.v1.txt"
OUT_FILE="word-test.v1.normalized.txt"

sed -e 's/	/ /g' ./$IN_FILE > ./$OUT_FILE

