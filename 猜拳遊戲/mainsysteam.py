"""
這是猜拳遊戲主系統!
本系統用於整合其他附屬模組。
遊戲流程如下:
1.玩家出拳
2.AI出拳
3.判斷勝負
4.顯示雙方出的拳
5.顯示勝負
"""

# 模組區
from random import choice
from tkinter import *

def display_AI():
    """ 展示AI出的拳 """

    txt_AI.config(text=f'AI:{ai}',font=('標楷體',35,'bold'))

def mora():
    """ AI隨機出拳 """

    global ai
    ai=choice(item)

def scissors():
    """ 出剪刀 """

    global player
    player=item[0]
    comply()

def stone():
    """ 出石頭 """

    global player
    player=item[1]
    comply()

def paper():
    """ 出布 """

    global player
    player=item[2]
    comply()

def display_player():
    """ 展示玩家出的拳 """

    txt_player.config(text=f'玩家:{player}',font=('標楷體',35,'bold'))

def judge():
    """ 判斷勝負 """

    global victory

    if ai == player:                                #平手
        victory=victory_type[2]

    elif (ai == item[0]) and (player == item[1]):   #勝利1(剪刀)
        victory=victory_type[0]

    elif (ai == item[0]) and (player == item[2]):   #敗北1(剪刀)
        victory=victory_type[1]

    elif (ai == item[1]) and (player == item[2]):   #勝利2(石頭)
        victory=victory_type[0]

    elif (ai == item[1]) and (player == item[0]):   #敗北2(石頭)
        victory=victory_type[1]

    elif (ai == item[2]) and (player == item[0]):   #勝利3(布)
        victory=victory_type[0]

    elif (ai == item[2]) and (player == item[1]):   #敗北3(布)
        victory=victory_type[1]

def display_victory():
    """ 展示勝負 """

    txt_judge.config(text=victory,font=('標楷體',40,'bold'))
    txt_judge.place(x=275,y=150)

def comply():
    """ 運行遊戲邏輯 """

    mora()
    judge()
    display_player()
    display_AI()
    display_victory()

# 系統區
item=('剪刀', '石頭', '布')                   #拳種
victory_type=('你贏了!', '你輸了!', '平手!')  #勝負類型
ai=None                                      #放AI出的拳
player=None                                  #放玩家出的拳
victory=None                                 #勝負結果

window=Tk()                     #視窗本體
window.title('猜拳遊戲')        #視窗標題
window.geometry('720x520')      #視窗大小
window.config(bg='#000000')     #視窗背景顏色

txt_AI=Label(window,text='',bg='#000000',fg='#00ff00',font=('標楷體',30,'bold'))                    #AI文字(放AI出拳的文字)
txt_AI.place(x=275,y=0)                                                                             #AI文字布局
txt_judge=Label(window,text='按下按鈕來猜拳!',bg='#000000',fg='#ff0000',font=('標楷體',30,'bold'))  #勝負文字(放初始訊息與輸贏的文字)
txt_judge.place(x=235,y=150)                                                                        #勝負文字布局
txt_player=Label(window,text='',bg='#000000',fg='#00ff00',font=('標楷體',30,'bold'))                #玩家文字(放玩家出拳的文字)
txt_player.place(x=275,y=300)                                                                       #玩家文字布局

options1=Button(window,text='剪刀',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=scissors)    #剪刀按鈕
options1.place(x=185,y=400)                                                                                 #剪刀按鈕布局
options2=Button(window,text='石頭',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=stone)       #石頭按鈕
options2.place(x=300,y=400)                                                                                 #石頭按鈕布局
options3=Button(window,text='布',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=paper)         #布按鈕
options3.place(x=415,y=400)                                                                                 #布按鈕布局

window.mainloop()