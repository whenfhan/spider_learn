from bs4 import BeautifulSoup
import re

# # 选择解析器
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)

# # 选择节点
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href
# ="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)

# # 提取节点信息
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href
# ="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title.name)
# print(soup.p.attrs)
# print(type(soup.p.attrs))
# print(soup.p.attrs['name'])

# # 嵌套选择
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

# # 关联选择
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)
# print('--------------children--------------')
# print(list(enumerate(soup.p.children)))
# print('--------------descendants--------------')
# print(list(enumerate(soup.p.descendants)))
# print('--------------parent--------------')
# print(soup.a.parent) # 直接父节点
# print('--------------parents--------------')
# print(list(enumerate(soup.a.parents))) # 祖先节点
# print('--------------next_sibling--------------')
# print(soup.a.next_sibling) # 下一个兄弟元素
# print('--------------previous_sibling--------------')
# print(soup.a.previous_sibling) # 上一个兄弟元素
# print('--------------next_siblings--------------')
# print(list(enumerate(soup.a.next_siblings))) # 后面的兄弟元素
# print('--------------previous_siblings--------------')
# print(list(enumerate(soup.a.previous_siblings))) # 前面的兄弟元素

# # 方法选择器
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# # 节点名查询
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
# print('-------------------------------------')
# # 属性查询
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# # 文本查询
# print('-------------------------------------')
# print(soup.find_all(text='Foo'))
# print(soup.find_all(text=re.compile('Foo')))

