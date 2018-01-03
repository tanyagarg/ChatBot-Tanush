import nltk
import csv

def hostel(sentence):
    hostel_name=['k',
'pg',
'j',
'l',
'iconic boys',
'e',
'i',
'a',
'g',
'iconic girls',
'h',
'b',
'c',
'd',
]
    name_of_hostel=' '
    token=sentence.split()
    flag=0
    n=len(token)
    for i in range(n):
        if(token[i]=='hostel'):
            flag=1
            for j in hostel_name:
                if(j[0]==token[i-1]):
                    name_of_hostel=token[i-1]    
                elif(i+1<n and j[0]==token[i+1]):
                    name_of_hostel=token[i-1]
    if(flag==1):
        return 1
    else:
        return 0

#hostel("i want to go to j hostel")