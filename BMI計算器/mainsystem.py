"""
這是BMI計算器主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from tkinter import *
import mybmi

def clear_all():
    """ 清除所有輸入框的內容 """

    weight_box.delete(0,END)
    height_box.delete(0,END)


def calculate_value():
    """ 計算數值 """

    height=float(height_box.get())
    weight=float(weight_box.get())
    bmi=round(mybmi.bmi_compute(weight,height),2)
    bmi_str=f'BMI:{bmi}'
    display_result(bmi_str)
    judge_BMI(bmi)


def display_result(x):
    """ 顯示BMI至畫面上 """

    result_txt.config(text=x)


def display_judge(x):
    """ 顯示判斷結果至畫面上 """

    judge_txt.config(text=x)


def judge_BMI(x):
    """ 判斷BMI """

    if mybmi.isLight(x):
        result=mybmi.bmi_norm['BMI < 18.5']
    elif mybmi.isNormal(x):
        result=mybmi.bmi_norm['18.5 <= BMI < 24']
    elif mybmi.isHeavy(x):
        result=mybmi.bmi_norm['24 <= BMI < 27']
    elif mybmi.isFat(x):
        result=mybmi.bmi_norm['27 <= BMI < 30']
    elif mybmi.isObesity(x):
        result=mybmi.bmi_norm['30 <= BMI < 35']
    elif mybmi.isOver(x):
        result=mybmi.bmi_norm['35 <= BMI']
    display_judge(result)


# 系統區
window=Tk()                     #視窗本體
window.title('BMI計算器')       #標題
window.geometry('720x520')      #大小
window.config(bg='#00ffff')     #背景顏色

hint_txt=Label(window,text='輸入身高和體重後按下按鈕',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'))      #操作提示文字
hint_txt.place(x=110,y=10)                                                                                      #操作提示文字之布局
weight_txt=Label(window,text='體重:',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'))                       #體重文字
weight_txt.place(x=150,y=290)                                                                                   #體重文字之布局
height_txt=Label(window,text='身高:',bg='#00ffff',fg='#000000',font=('標楷體',30,'bold'))                       #身高文字
height_txt.place(x=150,y=340)                                                                                   #身高文字之布局
result_txt=Label(window,text='BMI:???',bg='#00ffff',fg='#000000',font=('Arail',35,'bold'))                      #結果文字
result_txt.place(x=255,y=100)                                                                                   #結果文字之布局
judge_txt=Label(window,text='',bg='#00ffff',fg='#000000',font=('標楷體',35,'bold'))                             #判斷文字
judge_txt.place(x=295,y=200)                                                                                    #判斷文字之布局

weight_box=Entry(window,bg='#ffffff',fg='#000000',font=('Arail',20,'bold'))     #體重輸入框
weight_box.place(x=255,y=290)                                                   #體重輸入框之布局
height_box=Entry(window,bg='#ffffff',fg='#000000',font=('Arail',20,'bold'))     #身高輸入框
height_box.place(x=255,y=340)                                                   #身高輸入框之布局

calculate=Button(window,text='計算',bg='#ffffff',fg='#000000',font=('新細明體',30,'bold'),command=calculate_value)      #計算鈕
calculate.place(x=270,y=400)                                                                                            #計算鈕之布局
clear=Button(window,text='清除',bg='#ffffff',fg='#000000',font=('新細明體',30,'bold'),command=clear_all)                #清除鈕
clear.place(x=390,y=400)                                                                                                #清除鈕之布局

window.mainloop()