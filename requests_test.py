from email import header
import requests
import re

# # requests返回类型
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# # get不带参数
# r = requests.get('http://httpbin.org/get')
# print(r.text)

# # get带参数
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json()) # 将str转dict

# # get自定义请求头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(r.text)

# # 抓取二进制数据 & 保存文件
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# # post用法
# data = {'name': 'germey', 'age': '22'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

# # 响应信息
# r = requests.get('http://www.baidu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

# # 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# # 显示Cookies
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# # 使用真实Cookies
# headers = {
#     'Cookie': '_zap=6282f952-bda3-4e7a-9124-f7328f4c2523; d_c0="AKDQek390RGPTiZs7MEQq5EB5nGUORB_0yo=|1598929930"; _ga=GA1.2.298503101.1598929935; _9755xjdesxxd_=32; YD00517437729195:WM_TID=3OuzEF5xFmVEUBBVAQM7b1QUMQc4LZ4P; q_c1=aa08f4e2aa854682bc15052c494d5c05|1614758816000|1606788913000; __utma=155987696.298503101.1598929935.1631257595.1631257595.1; __snaker__id=BI7ptwvBiuE3sWQT; _xsrf=WBYzrUqlVaMe8osF7v2uyFtM75RHRrUG; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1655348104,1655348378,1655368777,1655434977; captcha_session_v2=2|1:0|10:1655434975|18:captcha_session_v2|88:cU1ZRHczaS9aYyt5L0FjbE5BRlUxN1FiaysrL1BIeXdpK0crUDlXd0JyUE8zaUlBMkRsOEduai8vL3docDZJRw==|7a43d52506feb25c47302f17e2174f12a04befc98041d39025ea5fa8e4bb95ce; SESSIONID=tPqKhDgr9JNx9mm5rseXcIjmHrL4aqLBUa8uY2Llucj; JOID=UFoQA0Pj5yv57WwCVeFdtpivk9lDl7Bfuo8oYiLQrWKE3AtvZzsLjZnnawBYq57RUXYOge_7I4chj0dRirpTcEQ=; osd=W14WBk3o4y3842cGU-RTvZypltdIk7ZatIQsZCfepmaC2QVkYz0Og5LjbQVWoJrXVHgFhen-LYwliUJfgb5VdUo=; gdxidpyhxdE=jCAiGpJ7cgq+\BiT+68jVPIZhqTABRzR6GZwYRNKQIhRIInb85CHaEIx5PwLTrkeovbacTUc3YWlA9hmkgdr0kru7Jau56+MTUj7Ux2iSoSa4xdV64eOR6mL8ShGkNwliKZcexjV\e1w+0qn\TRqYNauH2pULtpe3+2n91YIhwpzEplX:1655435877574; YD00517437729195:WM_NI=s9Af+eOHTm/ArkFuE6gLAti/vQS2YPFXOdEgKrnmV1W4dEeuqEnSQmum06tGlGxa68sUhpj1ha1tpfs0YDWcCtvtILsfe9rxWz23Ow/jmEDlrY0bDghQ/RBCvJdP2X6hU3g=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6ee83d649b4b0b7a9ce4a95b48aa6d85b878a8badc14bafa7e58cf1708cacfeaab62af0fea7c3b92ab1e78f87aa6f8d989c8eae4bb2b58a96c83ea5948f95ec25b68f9dd3dc5c86888185c86d89aea28ed53b95ecaca6e87fb39ba2b4d467b7b300d7f74db099b882b534b18ba891e93bacbfff95f36eb1f097a5d66981acba95cc48b1baabdaf17495a6fed4ce7dedb6a3a6c768b2870083c76dac8fe1b3c149b696acb1b154f6b89bd4e637e2a3; z_c0="2|1:0|10:1655435004|4:z_c0|92:Mi4xV3lLZUJnQUFBQUFBb05CNlRmM1JFU2NBQUFDRUFsVk4tM3ZUWWdCakdLVnlzMV9CNEtYV0M4RXdsR0k5SnlfQVR3|e08082eeeba345fb2d1290f29e1d9f940750dc44cbb0f65a66333d237e68378e"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1655435007; tst=r; NOT_UNREGISTER_WAITING=1; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1655435104|1655434974',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# # 会话维持
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# # 请求对象
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# s = requests.Session()
# req = requests.Request('POST', url, data=dict, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)

