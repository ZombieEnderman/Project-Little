"""
這是檔案下載速率計算器主系統!
本系統用於整合其他附屬模組。
※公式如下:
    下載時間 = 檔案大小(換成位元) ÷ 傳輸速率
※傳輸速率差距為1,000、檔案大小差距為1,024
"""

# 模組區
from tkinter import *

# 系統區
capacity={'KB':1_024 * 8,
          'MB':1_024 * 1_024 * 8,
          'GB':1_024 * 1_024 * 1_024 * 8,
          'TB':1_024 * 1_024 * 1_024 * 1_024 * 8}       #檔案大小字典

transmission={'Kbps':1_000,
              'Mbps':1_000 * 1_000,
              'Gbps':1_000 * 1_000 * 1_000,
              'Tbps':1_000 * 1_000 * 1_000 * 1_000}     #傳輸速率字典

window=Tk()                           #視窗本體
window.title('檔案下載速率計算器')      #標題
window.geometry('720x520')            #大小
window.config(bg='#ffffff')           #背景顏色

hint_txt1=Label(window,text='1.輸入大小與速率',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))#操作提示文字1
hint_txt1.place(x=240,y=10)#操作提示文字1之布局
hint_txt2=Label(window,text='2.選取單位',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))#操作提示文字2
hint_txt2.place(x=240,y=60)#操作提示文字2之布局
hint_txt3=Label(window,text='3.按下"計算"之按鈕',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))#操作提示文字3
hint_txt3.place(x=240,y=110)#操作提示文字3之布局
input_txt1=Label(window,text='檔案大小',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))#輸入框提示文字1
input_txt1.place(x=150,y=300)#提示文字1之布局
input_txt2=Label(window,text='傳輸速率',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))#輸入框提示文字2
input_txt2.place(x=150,y=350)#提示文字2之布局

box1=Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))#檔案大小輸入框
box1.place(x=270,y=300)#檔案大小輸入框之布局
box2=Entry(window,bg='#ffffff',fg='#000000',font=('Arial',20,'bold'))#檔案大小輸入框
box2.place(x=270,y=350)#檔案大小輸入框之布局

run=Button(window,text='計算',bg='#999999',fg='#ff0000',font=('新細明體',30,'bold'))    #執行鈕
run.place(x=300,y=430)                                                                 #執行鈕布局

window.mainloop()