import requests
from bs4 import BeautifulSoup
import re
import slackweb

SLACK_URL = 'https://hooks.slack.com/services/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'

# ダウンロード
url = 'https://atcoder.jp/contests'
response = requests.get(url)

# スクレイピング
soup = BeautifulSoup(response.content, "html.parser")

# 予定されたコンテスト
elems = soup.select("#contest-table-upcoming a")

slack = slackweb.Slack(SLACK_URL)


for elem in elems:
    print(slack.notify(text=elem.get_text()))