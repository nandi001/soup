import requests
from bs4 import BeautifulSoup

def get_links(url):
    # 发送HTTP GET请求获取网页内容
    response = requests.get(url)
    
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 提取所有的链接
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    
    return links

# 指定要爬取的网页URL
url = 'https://www.example.com'

# 获取网页中的链接
all_links = get_links(url)

# 打印提取到的链接
for link in all_links:
    print(link)
