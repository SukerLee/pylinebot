from linebot import LineBotApi
from linebot.models import TextSendMessage
line_bot_api = LineBotApi('vjiMCLIF9j7Eg2dyeP5oTniljQHL+2/kZSJ0D1dKS0bJ2BKokTBi8QDXj1NydhQX12kCIoGcAvPgrnRLNAV4WiyuweDRX8YCx+7t0NNHkpPbMDnoz6TK81U70tTjbTSSr0J/Yvuwvd/yp0i0W0jF7wdB04t89/1O/w1cDnyilFU=')
#push message to one user
line_bot_api.push_message('Uf92b6e174d84f112168054116db5d32a',
    TextSendMessage(text='吃飽了嗎?'))


#push message to multiple users
#line_bot_api.multicast(['user_id1', 'user_id2'],
#    TextSendMessage(text='Hello World!'))