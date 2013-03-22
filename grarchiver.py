import requests
import json
import io
import sys

##### Get Login & Password ###########

login = raw_input('Enter your username: ')
passwd = raw_input('Enter your password: ')

payload= {'accountType': 'HOSTED_OR_GOOGLE', 'Email': login, 'Passwd': passwd, 'service': 'reader', 'source': 'motdiem-grarchiver-alpha0'}
headers = {'Authorization': 'GoogleLogin auth= "Auth"'}  
url='https://www.google.com/accounts/ClientLogin'

r = requests.post(url,data=payload, headers=headers)

if r.status_code <> 200:
	print "Error Authenticating"
	sys.exit()

#### Retrieve Auth Token ########### 
loginresponse = r.text 
auth = loginresponse.split('\n')[2].split('=')[1] 

#### Fetch User Id ########### 
payload = {'ck': '20130316', 'client': 'GRARCHIVER'}
headers ={'Authorization': 'GoogleLogin auth='+auth} 
url='https://www.google.com/reader/api/0/user-info'

r = requests.get(url,params=payload, headers=headers)

if r.status_code <> 200:
	print "Error Retrieving userid"
	sys.exit()

userid=r.json().get('userId') 
print "Your userid is : " + userid 

#### Fetch Read Items ########### 
url = 'https://www.google.com/reader/api/0/stream/items/count'
payload = {'ck': '20130316', 'client': 'GRARCHIVER','s':'user/'+userid+'/state/com.google/read','a':'true'}


# Not retrieving read items anymore, just using continuation
#r = requests.get(url,params=payload, headers=headers)
#itemcount = int(r.text.split('#')[0].replace(',',''))
#print "You have : " + str(itemcount) + " read items - Now fetching them"
 
continuation=''
batchitems=[{}]
n = 1000


while True:
	url='https://www.google.com/reader/api/0/stream/contents/user/'+userid+'/state/com.google/read'
	payload = {'ck': '20130316', 'client': 'GRARCHIVER', 'output':'json',  'n': n, 'c':continuation}
	r = requests.get(url,params=payload, headers=headers)
	continuation = r.json().get('continuation')
	if continuation is None:
		break
	print 'doing next batch: ' + continuation
	for item in r.json().get('items'):
		batchitems.append(item)

print "retrieved " + str(len(batchitems)) + " items"

filename = raw_input('Enter your filename: ')

print "writing results to file"

with io.open(filename, 'a', encoding='utf-8') as f:
	f.write(unicode(json.dumps(batchitems, ensure_ascii=False)))
	
print "done - Thanks for using GRARchiver"


