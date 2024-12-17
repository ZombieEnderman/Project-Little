"""
這是檔案下載速率計算器主系統!
本系統用於整合其他附屬模組。
※公式如下:
    下載時間 = 檔案大小(換成位元) ÷ 傳輸速率
※傳輸速率差距為1,000、檔案大小差距為1,024
"""

# 模組區
from tkinter import *
import calculationsize as csize

def calculate_download():
    """ 計算下載時間 """

    size = float(box1.get())
    speed = float(box2.get())
    csize.calculate_size(None,size)
    csize.calculate_speed(None,speed)
    maintime = csize.file_size / csize.calculate_speed
    csize.calculate_time(maintime)
    display()


def clearall():
    """ 清空所有輸入框的內容 """

    box1.delete(0,END)
    box2.delete(0,END)


def display():
    """ 顯示結果 """

    result_txt.config(text=f'所需時間:{0}秒')

# 系統區
window=Tk()                           #視窗本體
window.title('檔案下載速率計算器')     #標題
window.geometry('720x520')            #大小
window.config(bg='#ffffff')           #背景顏色

hint_txt1 = Label(window,text='1.輸入大小與速率',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))       #操作提示文字1
hint_txt1.place(x=240,y=10)                                                                              #操作提示文字1之布局
hint_txt2 = Label(window,text='2.選取單位',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))             #操作提示文字2
hint_txt2.place(x=240,y=60)                                                                              #操作提示文字2之布局
hint_txt3 = Label(window,text='3.按下"計算"之按鈕',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))     #操作提示文字3
hint_txt3.place(x=240,y=110)                                                                             #操作提示文字3之布局
input_txt1 = Label(window,text='檔案大小',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))              #輸入框提示文字1
input_txt1.place(x=150,y=300)                                                                            #提示文字1之布局
input_txt2 = Label(window,text='傳輸速率',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))              #輸入框提示文字2
input_txt2.place(x=150,y=350)                                                                            #提示文字2之布局
result_txt = Label(window,text='所需時間:',bg='#ffdd00',fg='#000000',font=('標楷體',20,'bold'))             #結果文字
result_txt.place(x=260,y=200)                                                                            #結果文字之佈局

box1 = Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))       #檔案大小輸入框
box1.place(x=270,y=300)                                                     #檔案大小輸入框之布局
box2 = Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))       #檔案大小輸入框
box2.place(x=270,y=350)                                                     #檔案大小輸入框之布局

calculate = Button(window,text='計算',bg='#999999',fg='#ff0000',font=('新細明體',25,'bold'),command=calculate_download)    #計算鈕
calculate.place(x=367,y=430)                                                                                        #計算鈕之布局
clear = Button(window,text='清空',bg='#999999',fg='#ff0000',font=('新細明體',25,'bold'),command=clearall)              #完全清空鈕
clear.place(x=270,y=430)                                                                                            #完全清空鈕之布局

window.mainloop()