import requests
import json
from bs4 import BeautifulSoup

username = 'wipro-test-surya'
token = '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'

login = requests.get('https://api.github.com/search/repositories?q=github+api', auth = (username, token))

print(login)
print(type(login))
##soup = BeautifulSoup(login.content, "html.parser")
##print(soup)

##soup = BeautifulSoup(login.content, "html.parser")
##
##print(soup)


