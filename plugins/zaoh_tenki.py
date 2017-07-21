# -*- coding: utf-8 -*-
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slacker import Slacker
import slackbot_settings
import urllib.request
import json
import sys

### URLリクエストを行い、デコードするまでの関数 ###
def gethtml(uri):
    html = urllib.request.urlopen(uri)
    html = html.read().decode('utf-8')
    return html

### ↑をjson形式に変換するまでの関数 ###
def getjson(html):
    html = json.loads(html)
    return html

### 蔵王の天気情報(今日と明日)を取得 ###
@listen_to('天気')
def tenki(message):
    uri = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=040020'
    jsonfile = getjson(gethtml(uri))
    kekka = "----蔵王近辺の天気情報----\n"
    today = jsonfile['forecasts'][0]['telop']
    tomorrow = jsonfile['forecasts'][1]['image']['title']
    if '雨' in today or '雨' in tomorrow :
        iro = 'danger'
    elif '曇' in today or '曇' in tomorrow :
        iro = 'warning'
    else :
        iro = 'good'
    kekka += '今日の天気は %s \n' % (today)
    kekka += '明日の天気は %s \n' % (tomorrow)
    kekka += '----蔵王天気情報ここまで----'

    slack = Slacker(slackbot_settings.API_TOKEN)
    attachment = {
        'text' : kekka,
        'color': iro
    }
    slack.chat.post_message(
        'bot',
        '',
        as_user=True,
        attachments=[attachment]
    )
