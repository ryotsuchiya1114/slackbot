# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

if __name__ == '__main__':

    slack = Slacker(slackbot_settings.API_TOKEN)
    attachment = {
        'author_name': 'つちやりょう',
        'author_link': 'http://blog.bitmeister.jp/?p=3892',
        'title': 'PythonでSlackbotを作るよー',
        'color': '#1e2c5b'
    }

    slack.chat.post_message(
        'general',
        'ブログが更新されました',
        as_user=True,
        attachments=[attachment]
    )
