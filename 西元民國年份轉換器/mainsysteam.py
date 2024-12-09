"""
這是西元民國年份轉換器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import rocyear

# 系統區
window=Tk()                             #視窗本體
window.title('西元民國年份轉換器')      #標題
window.geometry('720x520')              #大小
window.config(bg='#ff0000')             #背景顏色

hint_txt=Label(window,text='輸入年份後按下按鈕',bg='#ff0000',fg='#0000ff',font=('標楷體',40,'bold'))    #操作提示文字
hint_txt.place(x=100,y=20)                                                                              #操作提示文字之布局
input_txt=Label(window,text='年份',bg='#ff0000',fg='#0000ff',font=('新細明體',30,'bold'))               #輸入框提示文字
input_txt.place(x=120,y=260)                                                                            #輸入框提示文字之布局

input_box=Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))      #輸入框
input_box.place(x=220,y=262)                                                    #輸入框之布局

roc_button=Button(window,text='轉西元',bg='#ffffff',fg='#000000',font=('新細明體',25,'bold'))   #西元鈕
roc_button.place(x=210,y=360)                                                                   #西元鈕之布局
ad_button=Button(window,text='轉民國',bg='#ffffff',fg='#000000',font=('新細明體',25,'bold'))    #民國鈕
ad_button.place(x=355,y=360)                                                                    #民國鈕之布局

window.mainloop()