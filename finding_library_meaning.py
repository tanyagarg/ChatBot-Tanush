import nltk
import csv

def library(sentence):
    lib_meaning=['study', 'athenaeum', 'atheneum','newspaper','books', 'novel','bibliotheca', 'book collection', 'application', 'review', 'inquiry', 'debate', 'research', 'essay', 'album', 'novel', 'publication', 'dictionary', 'scan', 'study', 'gather', 'see', 'know']
    token=sentence.split()
    lib_source=[]
    flag=0
    n=len(token)
    for i in range(n):
        #print token[i]
        for k in lib_meaning:
            lib_split=k.split()
            #print lib_split
            if(token[i]==k):
                lib_source.append(token[i])
                flag=1
            elif(len(lib_split)>1):
                m=len(lib_split)
                l=0;
                while(m>0):
                    if(i+l<len(token) and token[i+l]==lib_split[l]):
                        l=l+1
                        m=m-1
                    else:
                        break
                if(m==0):
                    x=len(lib_split)
                    for l in range(x):
                        lib_source.append(token[i+l])
                        flag=1
            if(flag==1):
                break
    if(lib_source):
        return lib_source
    else:
        return 0
library('this is a ')