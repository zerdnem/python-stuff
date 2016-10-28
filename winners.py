import requests, re, json
from bs4 import BeautifulSoup

url = "https://dbrand.com/winners"
req = requests.get(url)
data = req.text
soup = BeautifulSoup(data, 'lxml')
winners = soup.find_all("div", class_="attr name")

accounts = []
for yt in winners:
	accounts.append(yt)
account = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(accounts))
yt_account = account 

names = []
for user in accounts:
	patterns = re.sub('<[^>]*>', '',  str(user))
	names.append(patterns)
name = names[1:]

final = dict(zip(name, yt_account))

for value, key in final.iteritems():
	v = value.strip('\n')
	k = key.strip('\n')
	print(v + ' => ' + k)
