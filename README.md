# pylinebot
LINE訊息機器人Python版

from linebot import LineBotApi
from linebot.models import TextSendMessage
line_bot_api = LineBotApi('你的Channel access token')

#push message to one user
line_bot_api.push_message('使用者ID',
    TextSendMessage(text='訊息內容'))

#發訊息給多個使用者
#push message to multiple users 
#line_bot_api.multicast(['user_id1', 'user_id2'],
#    TextSendMessage(text='Hello World!'))
