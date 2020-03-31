import requests
import  re
import base64

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.post(url, auth = (username, password))
# content = response.text
# print(content) # discovered source code index-source.html

# response = session.post(url + 'index-source.html', auth = (username, password))
# content = response.text
# print(content) discovered a base64 encoded secret 3d3d516343746d4d6d6c315669563362

encoded = '3d3d516343746d4d6d6c315669563362'
ReverseBase64secret =  bytes.fromhex(encoded)
Base64secret = ReverseBase64secret[::-1]
secret = base64.b64decode(Base64secret).decode("utf-8")
# print(secret)

response = session.post(url, data = {"secret": secret, "submit" : "submit"}, auth = (username, password))
content = response.text
# print(content)
print(re.findall("The password for natas9 is (.*)",content)[0])