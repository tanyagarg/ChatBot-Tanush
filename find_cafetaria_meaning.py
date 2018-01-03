import nltk
def cafetaria(sentence):
    cafe_meaning=['snack bar', 'chuck wagon', 'mobile kitchen','hunger', 'snack shop', 'caftan', 'criteria', 'caveats', 'caveat', 'coterie', 'cafeteria', 'bistro', 'coffee shop', 'diner', 'joint', 'feed', 'chew', 'dine', 'inhale', 'bite','cafe','hungry' ,'sip', 'alcohol', 'cup', 'liquor', 'refreshment', 'eager', 'keen', 'greedy', 'starved', 'ravenous', 'eat', 'snacks', 'fast food', 'indian', 'cuisine', 'lunch', 'dinner', 'breakfast']
    '''with open('cafe_meaning.csv','r') as csv1:
         sp=csv.reader(csv1)
         for i in sp:
             cafe_meaning.append(i)
             print i
    csv1.close()
    '''
    token=sentence.split()
    cafe_source=[]
    flag=0
    n=len(token)
    for i in range(n):
        '''for j in cafe_meaning:
            print j
            print "hiiiiiiii"'''
        for k in cafe_meaning:
            #print k
            cafe_split=k.split()
            if(token[i]==k):
                cafe_source.append(token[i])
                flag=1
            elif(len(cafe_split)>1):
                m=len(cafe_split)
                l=0;
                while(m>0):
                    if(i+l<len(token) and token[i+l]==cafe_split[l]):
                        l=l+1
                        m=m-1
                    else:
                        break
                if(m==0):
                    x=len(cafe_split)
                    for l in range(x):
                        cafe_source.append(token[i+l])
                        flag=1
            if(flag==1):
                break
    if(cafe_source):
        return cafe_source
    else:
        return 0
