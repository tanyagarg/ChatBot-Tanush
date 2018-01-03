import sys
from calling_functions_keyword import keywords
import re
from check_if_user_has_entered_source_and_dest import source_destination
#print sys.argv[1]
sentence=sys.argv[1]
#sentence="from e_block to library";
sentence=re.sub(r';', ' ', sentence)
#print sentence
x=source_destination(sentence)
print x

if x[0]=='0':
    y=keywords(sentence)
    print(y)
else:
    print(x)
