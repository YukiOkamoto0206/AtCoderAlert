import requests
from bs4 import BeautifulSoup
import re

# ダウンロード
url = 'https://atcoder.jp/contests'
response = requests.get(url)

# スクレイピング
soup = BeautifulSoup(response.content, "html.parser")
# 予定されたコンテスト
elems = soup.select("#contest-table-upcoming")


print(elems)
