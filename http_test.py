import requests
# url = "https://httpbin.org/get"
# resp = requests.get(url)
# print(resp.json())

r = requests.get('https://netology.ru/')
print(r.json())