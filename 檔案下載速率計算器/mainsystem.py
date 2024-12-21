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

    size = float(box1.get())                        #獲取檔案輸入框的內容
    speed = float(box2.get())                       #獲取速率輸入框的內容
    size_unit = capacity_tuple[x.get()]             #獲取檔案選擇鈕的內容
    speed_unit = transmission_tuple[y.get()]        #獲取速率選擇鈕的內容
    csize.calculate_size(size_unit,size)
    csize.calculate_speed(speed_unit,speed)
    maintime = csize.file_size / csize.velocity
    csize.calculate_time(maintime)
    format_time(csize.time)
    display(csize.time)


def clearall():
    """ 清空所有輸入框的內容 """

    box1.delete(0,END)
    box2.delete(0,END)
    result_txt.config(text="所需時間:")


def display(x):
    """ 顯示結果 """

    result_txt.config(text=f'所需時間:\n{x}')


def format_time(x):
    """ 格式化時間 """    

    if not(x[0]) and not(x[1]):
        csize.time = f'{x[2]}秒'
    elif not(x[0]):
        csize.time = f'{x[1]}分{x[2]}秒'
    else:
        csize.time = f'{x[0]}小時{x[1]}分{x[2]}秒'

# 視窗區
window = Tk()                         #本體
window.title('檔案下載速率計算器')     #標題
window.geometry('720x520')            #大小
window.config(bg='#ffffff')           #背景顏色

# 容器區
capacity_tuple = tuple(z for z in csize.capacity)           #檔案大小元組
transmission_tuple = tuple(z for z in csize.transmission)   #傳輸速率元組
x = IntVar()                                                #整數物件1
y = IntVar()                                                #整數物件2

# 文字標籤區
input_txt1 = Label(window, text='檔案大小', bg='#ffffff', fg='#000000', font=('標楷體', 20, 'bold'))         #檔案標籤
input_txt1.place(x=150,y=170)                                                                                #檔案標籤之布局
input_txt2 = Label(window, text='傳輸速率', bg='#ffffff', fg='#000000', font=('標楷體', 20, 'bold'))         #速率標籤
input_txt2.place(x=150,y=300)                                                                                #速率標籤之布局
result_txt = Label(window, text='所需時間:', bg='#ffdd00', fg='#000000', font=('標楷體', 20, 'bold'))        #結果標籤
result_txt.place(x=250,y=50)                                                                                 #結果標籤之佈局

# 輸入框區
box1 = Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 20, 'bold'))    #檔案輸入框
box1.place(x=270,y=170)                                                         #檔案輸入框之布局
box2 = Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 20, 'bold'))    #速率輸入框
box2.place(x=270,y=300)                                                         #速率輸入框之布局

# 單選鈕區
for z in range(len(capacity_tuple)):        #檔案選擇鈕
    capacity = Radiobutton(window, text=capacity_tuple[z], bg='#ffffff', fg='#000000', font=('Arial',10,'bold'), variable=x, value=z)
    capacity.place(x=260+(z*45), y=230)

for z in range(len(transmission_tuple)):    #速率選擇鈕
    transmission = Radiobutton(window, text=transmission_tuple[z], bg='#ffffff', fg='#000000', font=('Arial',10,'bold'), variable=y, value=z)
    transmission.place(x=155+(z*60), y=350)

# 按鈕區
calculate = Button(window, text='計算', bg='#999999', fg='#ff0000', font=('新細明體',25,'bold'), command=calculate_download)    #計算鈕
calculate.place(x=367,y=430)                                                                                                    #計算鈕之布局
clear = Button(window, text='清空', bg='#999999', fg='#ff0000', font=('新細明體',25,'bold'), command=clearall)                  #清空鈕
clear.place(x=270,y=430)                                                                                                        #清空鈕之布局

window.mainloop()