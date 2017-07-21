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

### 株価取得用関数 ###
### 改行区切りで配列化し、最後から2つめの最新株価情報を取得 ###
### その後、","区切りで配列化し、先頭から2番めの要素を返す ###
def getkabuka(code):
    url = 'https://www.google.com/finance/getprices?p=1h&i=300&x=TYO&q=%s' % (code)
    html = gethtml(url).split("\n")
    html = html[-2].split(",")[1]
    return html

### 株価の取得 ###
@listen_to('[0-9][0-9][0-9][0-9]')
def kabuka(message):
    meigara = message.body['text']
    html = getkabuka(meigara)
    f = open("/home/beck/stocklist.csv")
    companyList = f.readlines()
    f.close()
    for line in companyList:
        if line.find(meigara) >= 0:
            company = line.split(",")[1]
            break
        else:
            company = '不明な企業'
    kekka = '----現在の【%s】の株価----\n' % (company)
    kekka += html + "\n"
    message.send(kekka)
