from calling_functions_keyword import keywords
import nltk
import csv
destination=["to","for","go","reach","is"]
source=["from","at"]
check_point=[]
current_source=" "
current_destination=" "

sentence="where is cos. please help me reach.";
sentence =sentence.replace(".", "") #*************************************************************************************
def path(sentence):
    token=nltk.word_tokenize(sentence)
    flag=0
    for i in token:
        if i in destination and flag==0:
            flag=1
        elif flag==1:
            with open('checkpoints.csv','rb') as csv1:
                sp=csv.reader(csv1)
                for j in sp:
                    if j[0]==i:
                        check_point.append(i)
            csv1.close()
    for i in check_point:
        print i

def source_destination(sentence):
    # function to find the source and destination from users's sentence
    global current_source,current_destination
    token=nltk.word_tokenize(sentence)
    for i in range(0,len(token)):
        if token[i] in source:
            print"token"
            print token[i]
            with open('checkpoints.csv','rb') as csv1:
                sp=csv.reader(csv1)
                for k in sp:
                    print "llllllllllll"
                    print k[0]
                    print token[i+1]
                    if i+1<len(token) and token[i+1]==k[0]: #*****************************************************************************
                        current_source=k[0]
                        break
                    elif i+2<len(token) and token[i+2]==k[0]:
                        current_source=k[0]
                        break
        if token[i] in destination:
            print token[i]
            with open('checkpoints.csv','rb') as csv1:
                sp=csv.reader(csv1)
                for k in sp:
                    if i+1<len(token) and token[i+1]==k[0]: #*****************************************************************************
                        print "kkkkkk"
                        print token[i+1]
                        print k[0]
                        current_destination=k[0]
                        break
                    elif i+2<len(token) and token[i+2]==k[0]:
                        current_destination=k[0]
                        break    
            csv1.close();
    # here i am checking if the user has not submitted the correct source and destination .
    # from here we will call function from another program to find out the keywords so that we are able to find
    #correct source and destination
    if current_source==" ": # if user did not enter the source
        print "no source given"
    else:                   
        print current_source
    if current_destination==" ": #if user did not enter destination
        print "no destination given"
    else:                   
        print current_destination
        
    #here we are now findingg diffent keywords
    #-----------------------------------------------------------------------------#
    keywords(sentence)        
    while current_source==" " or current_destination==" ":
     if current_source==" ":
          a=raw_input("Where are u currently?")
          with open('checkpoints.csv','rb') as csv1:
                sp=csv.reader(csv1)
                for l in sp:
                    print l
                    if a==l[0]:
                     current_source=a;
          csv1.close()
     if current_destination==" ":
          b=raw_input("where do u want to go?")
          with open('checkpoints.csv','rb') as csv1:
                sp=csv.reader(csv1)
                for l in sp:
                    print l
                    print l
                    if b==l[0]:          
                        current_destination=b;
          csv1.close()
     print current_source
     print current_destination
source_destination(sentence)