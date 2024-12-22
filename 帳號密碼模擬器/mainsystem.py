"""
這是帳號密碼模擬器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import json as js
import os

def examine_account(account):
    """ 檢查帳戶是否存在 """
    if not os.path.exists(link):
        return False  # 帳戶不存在

    with open(link, 'r', encoding='utf-8') as file:
        # 檢查文件是否為空
        if os.path.getsize(link) == 0:
            return False  # 文件為空
        
        try:
            data = js.load(file)
        except js.JSONDecodeError:
            return False  # 如果 JSON 解析失敗

        return data.get("name") == account  # 檢查帳戶名是否存在於數據中

def build_account():
    """ 建立帳戶 """
    account = input_account.get()
    password = input_password.get()
    
    # 檢查文件是否存在，若不存在則創建
    if not os.path.exists(link):
        with open(link, 'w', encoding='utf-8') as file:
            js.dump({"name": account, "password": password}, file)  # 初始化為帳戶和密碼
            result_txt.config(text='帳戶建立成功')
            return

    # 檢查帳戶是否已存在
    if examine_account(account):
        result_txt.config(text='已存在的帳戶')
        return
    
    # 建立帳戶
    with open(link, 'r+', encoding='utf-8') as file:
        try:
            data = js.load(file) if os.path.getsize(link) > 0 else {}
        except js.JSONDecodeError:
            data = {}  # 如果 JSON 解析失敗，初始化為空字典

        # 更新數據結構
        data["name"] = account
        data["password"] = password

        file.seek(0)
        js.dump(data, file)
        file.truncate()  # 確保文件大小正確
        result_txt.config(text='帳戶建立成功')

def examine_password(account, password):
    """ 檢查密碼是否正確 """
    if not os.path.exists(link):
        return False  # 檔案不存在

    with open(link, 'r', encoding='utf-8') as file:
        # 檢查文件是否為空
        if os.path.getsize(link) == 0:
            return False  # 文件為空
        
        try:
            data = js.load(file)
        except js.JSONDecodeError:
            return False  # JSON解析失敗

        return data.get("password") == password

def log_account():
    """ 登入帳戶 """
    account = input_account.get()
    password = input_password.get()

    if not examine_account(account):
        result_txt.config(text='未存在的帳戶')
        return

    if examine_password(account, password):
        result_txt.config(text='歡迎回來')
    else:
        result_txt.config(text='密碼錯誤!')

# 系統區
link = "C:\\Users\\JOJO\\OneDrive\\桌面\\GitHub\\Project-Little\\帳號密碼模擬器\\user.json"

window = Tk()
window.title('模擬帳密系統')
window.geometry('720x520')
window.config(bg='#000000')

result_txt = Label(window, text='', bg='#000000', fg='#00ff00', font=('標楷體', 40, 'bold'))
result_txt.place(x=225, y=50)
account_txt = Label(window, text='帳號', bg='#000000', fg='#00ff00', font=('標楷體', 30, 'bold'))
account_txt.place(x=150, y=190)
password_txt = Label(window, text='密碼', bg='#000000', fg='#00ff00', font=('標楷體', 30, 'bold'))
password_txt.place(x=150, y=280)

input_account = Entry(window, bg='#ffffff', fg='#ff0000', font=('Arial', 20, 'bold'))
input_account.place(x=250, y=190)
input_password = Entry(window, bg='#ffffff', fg='#ff0000', font=('Arial', 20, 'bold'), show='*')
input_password.place(x=250, y=280)

log_button = Button(window, text='登入', bg='#ffffff', fg='#ff0000', font=('標楷體', 30, 'bold'), command=log_account)
log_button.place(x=250, y=350)
register_button = Button(window, text='註冊', bg='#ffffff', fg='#ff0000', font=('標楷體', 30, 'bold'), command=build_account)
register_button.place(x=400, y=350)

window.mainloop()