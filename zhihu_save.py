import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/hot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}
html = requests.get(url, headers=headers).text
print(html)
doc = pq(html)
print(items = doc('section .HotItem'))
items = doc('section .HotItem').items()
for item in items:
    question = item.find('.HotList-list').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()