# -*- coding: utf-8 -*-
## importする ##
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slacker import Slacker
import slackbot_settings

import urllib.parse
import urllib.request
import json
import sys

@respond_to('つかれた')
@respond_to('疲れた')
def cheer(message):
    message.reply('ファイト')

@listen_to('あきらめたら')
@listen_to('諦めたら')
def anzai(message):
    message.send('そこで試合終了ですよ。')

@listen_to('いいですか')
def reaction(message):
    message.react('+1')

### 入力したメッセージを受け取って表示する ###
@listen_to('バカ')
def baka(message):
    f = open("/home/beck/test.text", "w")
    f.write(message.body['user'])
    f.write(message.body['text'])
    f.close()
    text = message.body['text']
    message.reply(text)

"""
@listen_to("*")
def kakikomi(message):
    f = open("/home/beck/test.text", "w")
    f.write(message.body['user'])
    f.write(message.body['text'])
    f.close()
"""
