import threading
import arcpy  
import requests
import json
from datetime import datetime


# Disable warnings
requests.packages.urllib3.disable_warnings()

# Get Parameters
addfsURL = arcpy.GetParameterAsText(0)
interval = int(arcpy.GetParameterAsText(1))
deviceID = int(arcpy.GetParameterAsText(2))
quantity = int(arcpy.GetParameterAsText(3))
username = arcpy.GetParameterAsText(4)
password = arcpy.GetParameterAsText(5)

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
