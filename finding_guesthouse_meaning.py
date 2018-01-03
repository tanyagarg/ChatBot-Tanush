import nltk
import csv

def rest(sentence):
    rest_meaning=['break',
'comfort',
'rest',
'sleep',
'refresh',
'refreshment',
'respite',
'sleep',
'slumber',
'somnolence',
'doze',
'ease',
'leisure',
'relax',
'night stay',
'guest room',
'guest house',
'cubicle',
'lodging house'
]
    token=sentence.split()
    rest_source=[]
    flag=0
    n=len(token)
    for i in range(n):
        for k in rest_meaning:
            rest_split=k.split()
            if(token[i]==k):
                rest_source.append(token[i])
                flag=1
            elif(len(rest_split)>1):
                m=len(rest_split)
                l=0;
                while(m>0):
                    if(i+l<len(token) and token[i+l]==rest_split[l]):
                        l=l+1
                        m=m-1
                    else:
                        break
                if(m==0):
                    x=len(rest_split)
                    for l in range(x):
                        rest_source.append(token[i+l])
                        flag=1
            if(flag==1):
                break
    if(rest_source):
        return rest_source
    else:
        return 0