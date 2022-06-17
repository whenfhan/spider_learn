import re

# # match从头开始匹配
# # 匹配失败返回None
# # 匹配成功SRE_Match对象
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

# # match匹配字符串中提取子串
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('Hello\s(\d+)\s(\d+)\s\w{10}', content)
# print(result)
# print(result.group(1))
# print(result.group(2))

# # 贪婪匹配 (尽可能多匹配)
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('.*(\d+).*', content)
# print(result)
# print(result.group(1))  # 7
# #非贪婪匹配 (尽可能少匹配)
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('.*?(\d+).*', content)
# print(result)
# print(result.group(1))  # 1234567

# # (.)匹配任意字符
# content = '''Hello
# 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('.*?(\d+).*', content) # None, (.)不能匹配换行符
# print(result)
# result = re.match('.*?(\d+).*', content, re.S) # re.S使(.)能匹配所有字符
# print(result)
# print(result.group(1))  # 1234567

# re.I      使匹配对大小写不敏感
# re.L      做本地化识别匹配
# re.M      多行匹配，影响^和$
# re.S      使(.)能匹配所有字符
# re.U      根据Unicode字符集解析字符，影响\w、\W、\b和\B
# re.X      该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解

# # 转义匹配
# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result)

# # search用法
# # 匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.search('\d+', content)
# print(result)

# # findall用法
# # 返回所有匹配成功的值
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))

# # sub用法
# # 替换
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)

# # commpile用法
# # 编译乘正则表达式对象
# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern = re.compile(' \d{2}:\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)