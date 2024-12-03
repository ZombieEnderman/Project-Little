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

window=Tk()
window.title('檔案下載速率計算器')
window.geometry('720x520')
window.config(bg='#ffffff')

hint_txt1=Label(window,text='1.輸入大小與速率',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))
hint_txt1.place(x=240,y=10)
hint_txt2=Label(window,text='2.選取單位',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))
hint_txt2.place(x=240,y=60)
hint_txt3=Label(window,text='3.按下"計算"之按鈕',bg='#ffffff',fg='#000000',font=('標楷體',20,'bold'))
hint_txt3.place(x=240,y=110)

run=Button(window,text='計算',bg='#333333',fg='#ff0000',font=('新細明體',30,'bold'))
run.place(x=300,y=430)
window.mainloop()