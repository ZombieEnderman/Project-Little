"""
這是猜拳遊戲主系統!
本系統用於整合其他附屬模組。
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

def stone():
    """ 出石頭 """

    global player
    player=item[1]

def paper():
    """ 出布 """

    global player
    player=item[2]

def display_player():
    """ 展示玩家出的拳 """

    txt_player.config(text=f'你:{player}',font=('標楷體',35,'bold'))

def judge():
    """ 判斷輸贏 """

    if ai==item[0]:
        vict=victory[0]
    txt_judge.config(text=victory,font=('標楷體',40,'bold'))

# 系統區
item=('剪刀', '石頭', '布')     #拳種
victory=('你贏了!', '你輸了!')  #勝負種
ai=None                        #放AI出的拳
player=None                    #放玩家出的拳

window=Tk()                     #視窗本體
window.title('猜拳遊戲')         #視窗標題
window.geometry('720x520')      #視窗大小
window.config(bg='#00aa00')     #視窗背景顏色

txt_AI=Label(window,text='',bg='#00aa00',fg='#0000ff',font=('標楷體',30,'bold'))                   #AI文字(放AI出拳的文字)
txt_AI.pack(side='top')                                                                           #AI文字布局
txt_judge=Label(window,text='按下按鈕來猜拳!',bg='#00aa00',fg='#0000ff',font=('標楷體',30,'bold'))  #勝負文字(放初始訊息與輸贏的文字)
txt_judge.pack(side='top')                                                                        #勝負文字布局
txt_player=Label(window,text='',bg='#00aa00',fg='#0000ff',font=('標楷體',30,'bold'))               #玩家文字(放玩家出拳的文字)
txt_player.pack(side='top')                                                                       #玩家文字布局

options1=Button(window,text='剪刀',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=scissors)    #剪刀按鈕
options1.pack(side='bottom')                                                                               #剪刀按鈕布局
options2=Button(window,text='石頭',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=stone)       #石頭按鈕
options2.pack(side='bottom')                                                                               #石頭按鈕布局
options3=Button(window,text='布',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=paper)         #布按鈕
options3.pack(side='bottom')                                                                               #布按鈕布局

window.mainloop()