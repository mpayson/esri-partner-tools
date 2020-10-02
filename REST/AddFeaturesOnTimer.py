import threading
import sys
#import arcpy  
import requests
import json
from datetime import datetime


# Disable warnings
requests.packages.urllib3.disable_warnings()

# Get Parameters
addfsURL = str(sys.argv[1])
interval = int(sys.argv[2])
deviceID = int(sys.argv[3])
quantity = int(sys.argv[4])
username = str(sys.argv[5])
password = str(sys.argv[6])

# Generate Token
tokenURL = 'https://www.arcgis.com/sharing/rest/generateToken'
params = {'f': 'pjson', 'username': username, 'password': password, 'referer': 'http://www.arcgis.com'}
r = requests.post(tokenURL, data = params, verify=False)
response = json.loads(r.content)
token = response['token']

# define timer
def fireTimer():
  threading.Timer(interval, fireTimer).start()

  #get timestamp
  noww = datetime.now()
  dateTimeNow = str(noww)

  attr = [{"attributes":{"pk":deviceID, "amount":quantity, "datetime1":dateTimeNow}}]
  params = {"features": json.dumps(attr), 'token': token, 'f': 'json'}
  r = requests.post(addfsURL, data = params, verify=False)

  print(r.json)

fireTimer()
