import urllib
import urllib2
import json
import os
import time
import re
from datetime import datetime, timedelta
import sys
import base64
headers = {'Accept': 'application/json', 'Authorization': 'Basic YzY2YjViZmUtYzNkZC00MjIxLTg3ZDMtYTUwYTc5MWNlZGUxOmZmZTMzODkwLWY4NTktNDA0Zi1iODc2LThmNGU5ODFjYTJiOQ== ', 'User-Agent': 'Mozilla 5.0'}
ip_list = [line.rstrip('\n') for line in open('filename.txt')]
for ip in ip_list:
  url_req = "https://api.xforce.ibmcloud.com/ipr/"+ip
  req = urllib2.Request(url_req, None, headers)
  response = urllib2.urlopen(req).read()
  response_json = json.loads(response)
  print "THE RESULTS FOR THE IP "+ip+ " :"
  if 'score' in response_json:
    print "The risk score for "+ip+ " is "+str(response_json['score'])
  else:
    print "No Score"
  if 'geo' in response_json:
    if 'country' in response_json['geo']:
      print "The country for "+ip+ " is "+str(response_json['geo']['country'])
    else:
      print "No Country"
  else:
    print "No Country"
  if 'cats' in response_json:
    if 'Scanning IPs' in response_json['cats']:
      print "The Scanning IPs for "+ip+ " is "+str(response_json['cats']['Scanning IPs'])
    else:
      print "No Scanning IPs"
    if 'Bots' in response_json['cats']:
      print "The Bots for "+ip+ " is "+str(response_json['cats']['Bots'])
    else:
      print "No Bots"
  else:
    print "No Cats"
  print "\n"
