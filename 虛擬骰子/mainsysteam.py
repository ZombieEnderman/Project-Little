"""
這是虛擬骰子主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from random import randint as scope
from tkinter import *

def sides():
    """ 擲骰子 """

    result=scope(1,6)
    txt.config(text=result,font=('Arial',50,'bold'))

# 系統區
window=Tk()
window.title('虛擬骰子')
window.geometry('720x520')
window.config(bg='#000000')

txt=Label(window,text='按下按鈕來擲骰子!',bg='#000000',fg='#00ff00',font=('標楷體',30,'bold'))
txt.pack(side='top')

run=Button(window,text='擲骰子',bg='#ffffff',fg='#ff0000',font=('標楷體',30,'bold'),command=sides)
run.pack(side='bottom')

window.mainloop()