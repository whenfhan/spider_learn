import re
from matplotlib.pyplot import getp
import requests

def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if(response.status_code == 200):
        return response.text
    return None

def getRank(html):
    result = re.findall('<li>.*?<em class="">(\d+).*?alt="(.*?)"', html, re.S)
    return result

def main():
    rank = []
    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='
        html = getPage(url)
        rank.append(getRank(html))
    print(rank)
    

if __name__ == '__main__':
    main()