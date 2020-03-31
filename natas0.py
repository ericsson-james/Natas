#!/usr/bin/env python

import requests
import  re

username = 'natas0'
password = username


url = 'http://%s.natas.labs.overthewire.org/' % username

#response = requests.get(url) ## The request made without authentication
#print(response) ##returned a 401 because we didn't auth
#print(response.text) ## adds verbosity to the 401 error.

response = requests.get(url, auth = (username, password))
#print(response.text)  ## All of the html.
content = response.text

print(re.findall('<!--The password for natas1 is (.*) -->', content)[0])
