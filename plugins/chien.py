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

### 東京メトロの遅延情報取得 ###
@listen_to('遅延')
def chien(message):
    dict = {"odpt.Railway:TokyoMetro.Fukutoshin":"副都心線", "odpt.Railway:TokyoMetro.Yurakucho":"有楽町線", "odpt.Railway:TokyoMetro.Ginza":"銀座線", "odpt.Railway:TokyoMetro.Tozai":"東西線", "odpt.Railway:TokyoMetro.Hanzomon":"半蔵門線", "odpt.Railway:TokyoMetro.Hibiya":"日比谷線", "odpt.Railway:TokyoMetro.Namboku":"南北線", "odpt.Railway:TokyoMetro.Chiyoda":"千代田線", "odpt.Railway:TokyoMetro.Marunouchi":"丸ノ内線"}
    ### 特定の路線の運行情報を取得する場合 ###
    # 'https://api.tokyometroapp.jp/api/v2/datapoints?rdf:type=odpt:TrainInformation&odpt:railway=odpt.Railway:TokyoMetro.Fukutoshin&acl:consumerKey=44a78738100c7b4f9a809dc44901edb5020f44329a53229a429b27a3a5a9e0b9'
    #メトロすべての運行情報を取得する
    uri ='https://api.tokyometroapp.jp/api/v2/datapoints?rdf:type=odpt:TrainInformation&acl:consumerKey=44a78738100c7b4f9a809dc44901edb5020f44329a53229a429b27a3a5a9e0b9'
    jsonfile = getjson(gethtml(uri))
    #返ってきたjsonファイルの要素数（メトロの路線数）をカウントする
    count = len(jsonfile)
    kekka = "----東京メトロ遅延情報----\n"

    for i in range(count):
        line = dict[ jsonfile[i][ 'odpt:railway' ] ]
        kekka += '■東京メトロ%sは  *%s* \n' % (line, jsonfile[i][ 'odpt:trainInformationText' ])
    kekka += "----東京メトロここまで----\n"

    ### JRの運行情報 ###
    uri2 = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
    jsonfile = getjson(gethtml(uri2))
    count = len(jsonfile)
    kekka += "----JR東日本遅延情報----\n"
    for i in range(count):
        if jsonfile[i]['company'] == 'JR東日本':
            kekka += jsonfile[i]['name'] + "\n"
    kekka += "----JR東日本ここまで----"
    message.send(kekka)
