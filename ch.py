"""
import sys
import  string

"""
import requests, json,string,sys
a=sys.argv[1]
#print(a)
#a="can_i_get_loan_?"
a = str.replace(a, '_', ' ')
#print(a)
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e274fbace69c4b9c9fe83c690fd90179',
}
knowledgebases = 'cc21ea14-28d4-4a88-9ed4-713654e79219'
url = "https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/"+knowledgebases+"/generateAnswer"
data = {"question": "hi?","top": 1}
data['question']=a
r = requests.post(url, data=json.dumps(data), headers=headers)
#print(r.status_code)
#a=r.answer
#print(r.json())
f=r.json()
#print(f['answers'][0]['answer'])
i=f['answers'][0]['score']
#i=10
#print i
#print "fufufufuf"
#print(f['answers'][0]['answer'])
#print(len(f['answers'][0]['answer']))
s=''
#print(f['answers'][0]['answer'])
#for i in range(0,int(len(int((f['answers'][0]['answer'])))/2)):
#    print(i)
if(i>10.00):
    print(f['answers'][0]['answer'])
else:
    print("sorry")

