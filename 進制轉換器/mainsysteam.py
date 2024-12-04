"""
這是進制轉換器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *

def binary():
    """ 轉二進位 """

    var=bin(int(input_value.get()))
    result_txt.config(text=f'二進位:\n{str(var)[2:]}')


def octal():
    """ 轉八進位 """

    var=oct(int(input_value.get()))
    result_txt.config(text=f'八進位:\n{str(var)[2:]}')


def hexadecimal():
    """ 轉十六進位 """

    var=hex(int(input_value.get()))
    result_txt.config(text=f'十六進位:\n{str(var)[2:]}')


# 系統區
window=Tk()                     #視窗本體
window.title('進制轉換器')      #標題
window.geometry('720x520')      #大小
window.config(bg='#000000')     #背景顏色

hint_txt=Label(window,text='輸入十進位數字後按下按鈕',bg='#000000',fg='#00ff00',font=('新細明體',20,'bold'))    #操作提示文字
hint_txt.place(x=200,y=10)                                                                                      #操作提示文字之布局
value_txt=Label(window,text='十進位',bg='#000000',fg='#00ff00',font=('新細明體',20,'bold'))                     #輸入框提示文字
value_txt.place(x=170,y=250)                                                                                    #輸入框提示文字之布局
result_txt=Label(window,text='',bg='#000000',fg='#00ff00',font=('新細明體',30,'bold'))                          #結果文字
result_txt.place(x=250,y=100)                                                                                   #結果文字之布局

input_value=Entry(window,bg='#ffffff',fg='#ff0000',font=('新細明體',20,'bold'))     #輸入框
input_value.place(x=260,y=250)                                                      #輸入框之布局

bin_button=Button(window,text='轉二進位',bg='#ffffff',fg='#000000',font=('新細明體',15,'bold'),command=binary)         #二進位鈕
bin_button.place(x=200,y=350)                                                                                          #二進位鈕之布局
oct_button=Button(window,text='轉八進位',bg='#ffffff',fg='#000000',font=('新細明體',15,'bold'),command=octal)          #八進位鈕
oct_button.place(x=310,y=350)                                                                                          #八進位鈕之布局
hex_button=Button(window,text='轉十六進位',bg='#ffffff',fg='#000000',font=('新細明體',15,'bold'),command=hexadecimal)  #十六進位鈕
hex_button.place(x=420,y=350)                                                                                          #十六進位鈕之布局

window.mainloop()