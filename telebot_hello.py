import telepot
import datetime
from pytz import timezone
KST = timezone('Asia/Seoul')
now = datetime.datetime.now(KST)



year = int(now.strftime('%Y'))
month = int(now.strftime('%m'))
day = int(now.strftime('%d'))
hour = int(now.strftime('%H'))
min = int(now.strftime('%M'))
sec = int(now.strftime('%S'))
w_day = ['월', '화', '수', '목', '금', '토', '일'][datetime.datetime(year, month, day).weekday()]




words = """ 
현재시각 - %d년 %d월 %d일(%s) %d시 %d분 %d초
Youtube 여러분. 반가워요! """ %(year, month, day, w_day , hour, min, sec)


chat_id = '-357408712'
my_token = '1210478577:AAFZTeyvx3DJU4b6WFzg9J6IhxnA4myEmrQ'
bot = telepot.Bot(my_token)
bot.sendMessage(chat_id, words)



