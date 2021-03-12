import requests
from bs4 import BeautifulSoup
import re
import slackweb
import datetime


def send_line_notify(notification_message):
    # LINEに通知する
    line_notify_token = '1Xvp4MDPkzvJ4g4U7YqYQS3P6WgkUCXLY951FkiCtuq'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': notification_message}
    requests.post(line_notify_api, headers = headers, data = data)


def send_slack_notify(notification_message):

    SLACK_URL = 'https://hooks.slack.com/services/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'
    slack = slackweb.Slack(SLACK_URL)
    slack.notify(text = notification_message)


# ダウンロード
url = 'https://atcoder.jp/contests'
response = requests.get(url)
# スクレイピング
soup = BeautifulSoup(response.content, "html.parser")
# 予定されたコンテスト
elems = soup.select("#contest-table-upcoming a")


# for elem in elems:
# send_slack_notify(elems[0].get_text())
# send_line_notify(elems[0].get_text())
# print(elems[0].get_text().getHour())
# print(elems[1].get_text())

# time_contest = datetime.datetime.elems[0]
time_string = elems[0].get_text()
# 取得したString型時刻をDate型に変換(2021-03-13 21:00:00)
time_date = datetime.datetime.strptime(time_string[:-5], '%Y-%m-%d %H:%M:%S')
print(time_date.month)
print(time_date.day)
print(time_date.hour)
print(time_date.minute)