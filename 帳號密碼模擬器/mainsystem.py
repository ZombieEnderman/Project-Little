"""
這是帳號密碼模擬器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import json as js

def examine_account (account):
    """ 檢查帳戶 """

    file = open(link,'r',encoding='utf-8')
    for s in file:
        if account in s:
            file.close()
            return True
    file.close()
    return False


def examine_password (password):
    """ 檢查密碼 """    

    file = open(link,'r',encoding='utf-8')
    file.close()


def build_account ():
    """ 建立帳戶 """

    account = input_account.get()
    if examine_account():
        pass


def log_account ():
    """ 登入帳戶 """

    account = input_account.get()
    if examine_account():
        pass

# 系統區
link = "C:\\Users\\ccwork\\Desktop\\程式\\Python\\user.json"

window = Tk()
window.title('模擬帳密系統')
window.geometry('720x520')
window.config(bg='#000000')

result_txt = Label(window,text='',bg='#000000',fg='#00ff00',font=('標楷體',40,'bold'))
result_txt.place(x=350,y=50)
account_txt = Label(window,text='帳號',bg='#000000',fg='#00ff00',font=('標楷體',30,'bold'))
account_txt.place(x=150,y=190)
password_txt = Label(window,text='密碼',bg='#000000',fg='#00ff00',font=('標楷體',30,'bold'))
password_txt.place(x=150,y=280)

input_account = Entry(window,bg='#ffffff',fg='#ff0000',font=('Arial',20,'bold'))
input_account.place(x=250,y=190)
input_password = Entry(window,bg='#ffffff',fg='#ff0000',font=('Arial',20,'bold'))
input_password.place(x=250,y=280)

log_button = Button(window,text='登入',bg='#ffffff',fg='#ff0000',font=('標楷體',30,'bold'),command=log_account)
log_button.place(x=250,y=350)
register_button = Button(window,text='註冊',bg='#ffffff',fg='#ff0000',font=('標楷體',30,'bold'),command=build_account)
register_button.place(x=400,y=350)

window.mainloop()