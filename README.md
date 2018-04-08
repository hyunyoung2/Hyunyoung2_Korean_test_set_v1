# Hyunyoung2 Korean test set v1

As you can readn the paper, the titel is **Efficient Estimation of Word Representations in Vector Space**.

They provide a test set for syntactic and semantic verification for word embedding and they also provide some module pretrained. 

So This repository is for translating the test set into Korean test using python app I made. 

Let's How to use this repository : 

First, If you just want to the test set translated into Korean, Use **Korean_word_test.v1.txt** under Korean directory. 

But if you want to Download the orginal test set, after that you want to translate another language. 

follow right this: 

First, move under Efficient_Estimation_of_Word_Representations_in_Vector_Space dir in English dir, and then run **Download_test_set.sh**

> ./Download_test_set.sh

 - If you want to turn the delimiter, tab character, into white space. run **normalized.sh**
 
 > ./normalized.sh
 
Second, install **googletrans** module to run python script.

> pip3 install googletrans

- In my case, I used python 3

I recommend you to use pyvenv(like virtualenv), when you run this python script. 

In my case, I used virtualenv of python3 with **pyvenv env** or **python3 -m venv evn**.

After enter the paper directory, run the script as follows:

>  python3 google_trans.py

- But If it doesn't work, check the file path and name like input file, 
- Currently, this setting is **word_test.v1.normailzed.text** that I used with **normalized.sh**
- Also, Another error is maybe cause of **googletrans's stability**

Finally, running the python script, **google_trans.py**, Check the file,**Korean_word_test_v1.txt** like this:

> vim Korean_word_test_v1.txt



## Reference 

 - [Python package googletrans 2.2.0](https://pypi.python.org/pypi/googletrans)
 
 - [googletrans's official site](http://py-googletrans.readthedocs.io/en/latest/)

 - [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781v3)

  - [The test set in the paper above](http://www.fit.vutbr.cz/~imikolov/rnnlm/word-test.v1.txt)
