import requests
import  re
import urllib
import base64
import binascii

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'


url = 'http://%s.natas.labs.overthewire.org' % username


session = requests.Session()
#response = session.get(url, auth = (username, password) )

# print(content)
#print(binascii.hexlify(base64.b64decode(urllib.parse.unquote(session.cookies['data']))).decode('utf-8'))
#ciphertext = "0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c"
##ciphertext is used in the php file

cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK" }
response = session.get(url, auth = (username, password), cookies = cookies )
content = response.text

print(re.findall("natas12 is (.*)<br>", content)[0])