print('requests РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

import requests

response = requests.get('https://vk.com/feed?payload=%7B%22user%22%3A%7B%22first_name%22%3A%22%22%2C%22last_name%22%3A%22%22%7D%7D')
x = response.ok
y = response.headers.items()
for a in y:
    print(a)

print(x)
print(y)

url = 'https://www.google.com/afadf'
response = requests.get(url)
print(f'Request to {url}. Status code is {response.status_code}.')
print(response.text)

Р


