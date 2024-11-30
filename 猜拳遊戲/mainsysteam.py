"""
這是猜拳遊戲主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from random import choice
from tkinter import *

def mora():
    """ AI出拳 """

    result=choice(item)
    txt.config(text=result,font=('Arial',50,'bold'))

# 系統區
item=('剪刀', '石頭', '布')

window=Tk()
window.title('猜拳遊戲')
window.geometry('720x520')
window.config(bg='#00aa00')

txt=Label(window,text='按下按鈕來猜拳!',bg='#00aa00',fg='#0000ff',font=('標楷體',30,'bold'))
txt.pack(side='top')

run=Button(window,text='猜拳',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'),command=mora)
run.pack(side='bottom')

window.mainloop()