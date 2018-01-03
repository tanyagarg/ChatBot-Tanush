#import finding_destination 
from find_cafetaria_meaning import cafetaria
from finding_administration import administration
from finding_guesthouse_meaning import rest
from finding_hostel_names import hostel
from finding_library_meaning import library
key=[]
def keywords(sentence):
    cafe=cafetaria(sentence)
    admin=administration(sentence)
    resting=rest(sentence)
    hostels=hostel(sentence)
    lib=library(sentence)
    key.append(cafe)
    key.append(admin)
    key.append(resting)
    key.append(hostels)
    key.append(lib)
    cnt=0
    flg=0
    for i in key:
        if i!=0 and cnt==0:
            x="cafee"
            flg=1
        elif i!=0 and cnt==1:
             x="admin"
             flg=1
        elif i!=0 and cnt==2:
            x="rest"
            flg=1
        elif i!=0 and cnt==3:
            x="hostels"
            flg=1
        elif i!=0 and cnt==4:
            x="lib"
            flg=1
        cnt=cnt+1
    if(flg==0):
        return 0
    else:
        return x        
#here now ui have to coonect to database and check


