"""
這是西元民國年份轉換器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import rocyear

def clear_all():
    """ 清空輸入框的內容 """

    input_box.delete(0,END)


def ad():
    """ 民國轉西元 """

    year=int(input_box.get())
    new_year=rocyear.ad_year(year)
    str_year=f"西元{new_year}年"
    display(str_year)


def roc():
    """ 西元轉民國 """

    year=int(input_box.get())
    new_year=rocyear.roc_year(year)
    str_year=f"民國{new_year}年"
    display(str_year)


def display(x):
    """ 顯示結果至畫面上 """

    result_txt.config(text=x)


# 系統區
window=Tk()                           #視窗本體
window.title('西元民國年份轉換器')    #標題
window.geometry('720x520')            #大小
window.config(bg='#ff0000')           #背景顏色

hint_txt=Label(window,text='輸入年份後按下按鈕',bg='#ff0000',fg='#0000ff',font=('標楷體',40,'bold'))  #操作提示文字
hint_txt.place(x=100,y=20)                                                                            #操作提示文字之布局
input_txt=Label(window,text='年份',bg='#ff0000',fg='#0000ff',font=('標楷體',30,'bold'))               #輸入框提示文字
input_txt.place(x=150,y=260)                                                                          #輸入框提示文字之布局
result_txt=Label(window,text='',bg='#ff0000',fg='#0000ff',font=('標楷體',30,'bold'))                  #結果文字
result_txt.place(x=270,y=150)                                                                         #結果文字之布局

input_box=Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))      #輸入框
input_box.place(x=250,y=262)                                                    #輸入框之布局

roc_button=Button(window,text='轉民國',bg='#ffffff',fg='#000000',font=('新細明體',25,'bold'),command=roc)           #民國鈕
roc_button.place(x=160,y=360)                                                                                       #民國鈕之布局
ad_button=Button(window,text='轉西元',bg='#ffffff',fg='#000000',font=('新細明體',25,'bold'),command=ad)             #西元鈕
ad_button.place(x=305,y=360)                                                                                        #西元鈕之布局
clear_button=Button(window,text='清除',bg='#ffffff',fg='#000000',font=('新細明體',25,'bold'),command=clear_all)     #清除鈕
clear_button.place(x=450,y=360)                                                                                     #清除鈕之布局

window.mainloop()