import requests
from bs4 import BeautifulSoup
import re
import slackweb
import datetime


def send_line_notify(notification_message):
    # LINEに通知する
    line_notify_token = 'TOKEN'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': '\n' + notification_message}
    requests.post(line_notify_api, headers = headers, data = data)


def send_slack_notify(notification_message):
    # slackに通知する
    SLACK_URL = 'URL'
    slack = slackweb.Slack(SLACK_URL)
    slack.notify(text = notification_message)


# ダウンロード
url = 'https://atcoder.jp/contests'
response = requests.get(url)
# スクレイピング
soup = BeautifulSoup(response.content, "html.parser")
# 予定されたコンテスト
elems = soup.select("#contest-table-upcoming a")


# 直近のデータ取得
time_string = elems[0].get_text()
# 取得したString型時刻をDate型に変換
time_date = datetime.datetime.strptime(time_string[:-5], '%Y-%m-%d %H:%M:%S')
contest_date = time_date.strftime('%m月%d日%H:%Mから')
contest_text = elems[1].get_text()
# コンテスト名省略 & ABC以外は通知しない
if 'AtCoder Beginner Contest' in contest_text :
    contest_text = contest_text.replace('AtCoder Beginner Contest', 'ABC')
else:
    exit()
send_line_notify(contest_date + '\n' + contest_text)
