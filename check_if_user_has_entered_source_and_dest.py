import nltk
import csv
#sentence="please help me reach a place to relax";
check_point=["f_block","g_block","cos","track","oat","lib","library","e_block","jaggi","academic_block"]
def source_destination(sentence):
    destination=["to","for","go","reach","is"]
    source=["from","at"]
    #check_point=[]
    #user_entered_dest_source=" "
    sentence =sentence.replace(".", "") #*************************************************************************************
    # function to find the source and destination from users's sentence
    
    global current_source,current_destination
    current_source=" "
    current_destination=" "
    token=nltk.word_tokenize(sentence)
    
    for i in range(0,len(token)):
        if token[i] in source:
           if i+1<len(token):
               if token[i+1] in check_point:
                  current_source=token[i+1]
           if i+2<len(token):
               if token[i+2] in check_point:
                  current_source=token[i+2]
        #we will now do the same for 
    for i in range(0,len(token)):
        if token[i] in destination:
           if i+1<len(token):
               if token[i+1] in check_point:
                  current_destination=token[i+1]
           if i+2<len(token):
               if token[i+2] in check_point:
                  current_destination=token[i+2]
                    
           """
           with open('checkpoints.csv','rb') as csv1:
                print "furr"
                sp=csv.reader(csv1)
                for k in sp:
                    if i+1<len(token) and token[i+1]==k[0]: #*****************************************************************************
                        current_source=k[0]
                        break
                    elif i+2<len(token) and token[i+2]==k[0]:
                        current_source=k[0]
                        break
           csv1.close();
           print "there"
           """
           
    
    """
        if token[i] in destination:
            with open('checkpoints.csv','rb') as csv2:
                sp=csv.reader(csv2)
                for k in sp:
                    if i+1<len(token) and token[i+1]==k[0]: #*****************************************************************************
                        current_destination=k[0]
                        break
                    elif i+2<len(token) and token[i+2]==k[0]:
                        current_destination=k[0]
                        break    
            csv2.close();
    """    
    # here i am checking if the user has not submitted the correct source and destination .
    # from here we will call function from another program to find out the keywords so that we are able to find
    #correct source and destination
    if current_source==" " and current_destination==" ":
        user_entered_dest_source="0"
    else:
        user_entered_dest_source="1"
    #print "kutti"
    if current_source==" ": # if user did not enter the source
       user_entered_dest_source=user_entered_dest_source+";1"
    else:                   
        user_entered_dest_source=user_entered_dest_source+";"+current_source
    #print "kamini"
    if current_destination==" ": #if user did not enter destination
        user_entered_dest_source=user_entered_dest_source+";1"
    else:                   
         user_entered_dest_source=user_entered_dest_source+";"+current_destination+";" 
    #here we are now findingg diffent keywords
    #---------------------------------------------------------------------------------------#
    #print "saali"
    #print user_entered_dest_source

    return user_entered_dest_source
#a=source_destination("i want to go to e_block from library")
#print a