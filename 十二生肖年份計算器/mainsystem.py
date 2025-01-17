"""
這是十二生肖年份計算器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import czodiac as cz

def clear():
    """ 清空輸入框 """    

    year_box.delete(0,END)
    display()


def display(x=''):
    """ 顯示結果 """    

    result_txt.config(text=x)


def calculate():
    """ 計算生肖 """    

    year = int(year_box.get())
    result = cz.calculate_zodiac(year)
    display(result)

# 視窗區
window = Tk()
window.title('十二生肖年份計算器')
window.geometry('500x360')
window.config(bg='#ffff00')

# 文字標籤區
result_txt = Label(window, text='', bg='#ffff00', fg='#000000', font=('標楷體', 40, 'bold'))
result_txt.place(x=180, y=80)
year_txt = Label(window, text='西元年份:', bg='#ffff00', fg='#000000', font=('新細明體', 25, 'bold'))
year_txt.place(x=100, y=150)

# 輸入框區
year_box = Entry(window, bg='#ffffff', fg='#000000', font=('標楷體', 20, 'bold'), width=10)
year_box.place(x=250, y=150)

# 按鈕區
calculate_button = Button(window, text='計算', bg='#00ff00', fg='#000000', font=('新細明體', 25, 'bold'), command=calculate)
calculate_button.place(x=150, y=220)
clear_button = Button(window, text='清空', bg='#00ff00', fg='#000000', font=('新細明體', 25, 'bold'), command=clear)
clear_button.place(x=250, y=220)

window.mainloop()