from bs4 import BeautifulSoup
import requests

# 1. 请求网页
website = "https://music.163.com/#/discover/toplist"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
response = requests.get(website,headers=headers)

# 2. 获取网页内容
content = response.text

# 3. 创建 BeautifulSoup
soup = BeautifulSoup(content,'lxml')

# 4. 获取歌曲列表
iframe = soup.find('iframe', id = "g_iframe")
table = soup.find('table', {
    'class': 'm-table'
})