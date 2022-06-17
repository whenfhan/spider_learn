from email.mime import base
from email.quoprimime import quote
from unittest import result
import urllib.response
import urllib.parse
import urllib.request
import urllib.error
import urllib.robotparser
import socket
import http.cookiejar

from requests import head

# # 不带参数请求
# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# # 带参数请求
# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data)
# print(response.read().decode('utf-8'))

# # 设置超时时间
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
#     print(response.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# # 自定义请求头
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# # 账号验证
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
# p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = urllib.request.HTTPBasicAuthHandler(p)
# opener = urllib.request.build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except urllib.error.URLError as e:
#     print(e.reason)

# # 代理
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e.reason)

# # Cookies
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)
# cookie.save(ignore_discard=True, ignore_expires=True)
# # 加载Cookies
# cookie2 = http.cookiejar.MozillaCookieJar()
# cookie2.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# for item in cookie2:
#     print(item.name + '=' + item.value)

# # 处理异常
# try:
#     response = urllib.request.urlopen('https://cuiqingcai.com/index.htm')
# except urllib.error.HTTPError as e:
#     print(e.reason, e.code, e.headers, seq='\n')
# except urllib.error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# # 返回异常对象
# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# # 解析连接
# result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# print(result.scheme, result[0], result.netloc, result[1], sep = '\n') # result是元组

# # 封装连接
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urllib.parse.urlunparse(data))

# # 构造GET请求参数
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urllib.parse.urlencode(params)
# print(url)

# # 反序列化
# # 转成字典类型
# query = 'name=germey&age=22'
# print(urllib.parse.parse_qs(query))
# # 转成元组组成的列表
# print(urllib.parse.parse_qsl(query))

# # 中文转URL编码
# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd=' + urllib.parse.quote(keyword)
# print(url)
# print(urllib.parse.unquote(url))

# # 读取robot.txt
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url('https://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'http://jianshu.com/search?=q=python&page=1&type=collections'))