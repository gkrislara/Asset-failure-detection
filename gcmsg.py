import sys
import json
import requests

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

coord=sys.argv[1]
lat=coord.split(':')[1][0:12]
lon=coord.split(':')[2][0:12]
msgflag=coord.split(':')[3][0]

url='https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?';
prox='prox='+lat+"%2C"+lon+"%2C10&mode=retrieveAddresses&maxresults=1&gen=9&app_id=__app_id__&app_code=__app_code__"; #get app id and code from here.com
url=url+prox;
location=requests.get(url)
y=json.loads(location.text)
msg=y['Response']['View'][0]['Result'][0]['Location']['Address']['Label']
#print(location.text)
print(y)
api_keym= # get the api key from way2sms website
secretm= # get the secret from way2sms website
usetype='stage'
phone= # phone number
senderid='QWERTYUI' # as trial version of waysms is used senderid is set randomly

message='the node is located at '+msg
if(msgflag == '1'):
    resp=sendPostRequest('http://www.way2sms.com/api/v1/sendCampaign',api_keym,secretm,usetype,phone,senderid,message)
    print(resp.text) 
