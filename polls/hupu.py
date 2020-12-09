import requests
from polls.models import Hupu

url = 'https://soccer.hupu.com/api/v1/fifa'
index = 1
for i in range(1):
    r = requests.get(url, params={'p': i+1}).json()
    data = r.get('data')
    for j in data:
        c = j.get('content')
        t = j.get('title')
        news = Hupu(hupu_title = t, hupu_content = c)
        news.save()
        index += 1
        # hupu.append({'title': t, 'content': c})

# print(hupu)