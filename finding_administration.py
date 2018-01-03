import nltk
import csv

def administration(sentence):
    admin_token=[]
    token=sentence.split()
    for i in token:
        if(i=='administration' or i=='admin'):
            return i
        else:
            return 0
