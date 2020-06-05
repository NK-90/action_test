import telepot
import datetime
from pytz import timezone
KST = timezone('Asia/Seoul')
now = datetime.datetime.now(KST)




def telebot(start1,start2):



    year = int(now.strftime('%Y'))
    month = int(now.strftime('%m'))
    day = int(now.strftime('%d'))
    w_day = ['월', '화', '수', '목', '금', '토', '일'][datetime.datetime(year, month, day).weekday()]
    left1 = datetime.datetime(year, month, day) -  datetime.datetime(start1[0], start1[1], start1[2])
    left2 = datetime.datetime(year, month, day) -  datetime.datetime(start2[0], start2[1], start2[2])
    left_days1 = left1.days +1
    left_days2 = left2.days +1



    word = """ 
    %d년 %d월 %d일 %s요일
Youtube 여러분. 반가워요! """ %(year, month, day, w_day)


    chat_id = '-357408712'
    my_token = '1210478577:AAFZTeyvx3DJU4b6WFzg9J6IhxnA4myEmrQ'
    bot = telepot.Bot(my_token)
    bot.sendMessage(chat_id, word)




    return




start1 = [2020, 3,  9]
start2 = [2020, 3, 25]
telebot(start1,start2)