with open("input.txt", "r", encoding='utf-8') as input:
    for url in input:
        url = url.strip()


import requests
r = requests.get(url).text
print(r)
print(len(r.splitlines()))


# Из imput.txt читаем url -> получаем текст по этому url + количество строк этого текста
