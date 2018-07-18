with open("input.txt", "r", encoding='utf-8') as input:
    for url in input:
        url = url.strip()

home_url = 'https://stepic.org/media/attachments/course67/3.6.3/'

import requests
text_from_url = requests.get(url).text
next_url = home_url + text_from_url

while(True):
    if(text_from_url.split()[0:1] == ['We']):
        break
    next_url = home_url + text_from_url
    print(next_url)
    text_from_url = requests.get(next_url).text

inp = text_from_url

with open('output.txt', 'w') as output:
    output.write(inp)
