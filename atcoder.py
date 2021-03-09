import requests
from bs4 import BeautifulSoup
import re

# ダウンロード
url = 'https://atcoder.jp/contests'
response = requests.get(url)

# スクレイピング
soup = BeautifulSoup(response.content, "html.parser")
# elems = soup.find_all("span", "user-blue")
# elems = soup.find_all("div", "contest-table-permanent") これしたい
elems = soup.find_all("div", "panel panel-default")


print(elems)
