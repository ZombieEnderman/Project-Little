"""
這是虛擬骰子主系統!
本系統用於整合其他附屬模組。
"""

# 模組區
from dice import *
from tkinter import *  # type: ignore


def refresh_screen() -> None:
    """刷新畫面"""
    dice_map = {
        "4面": four_sides,
        "6面": six_sides,
        "8面": eight_sides,
        "10面": ten_sides,
        "12面": twelve_sides,
        "20面": twenty_sides,
    }
    func = dice_map.get(var.get(), six_sides)
    result = str(func()[0])
    txt.config(text=result, font=('Arial', 40, 'bold'))


# 系統區
window: Tk = Tk()
window.title('虛擬骰子')
window.geometry('520x320')
window.config(bg="#FFFFFF")
window.iconbitmap("dice.ico")

txt = Label(window, text='按下按鈕來擲骰子!', bg="#FFFFFF",
            fg="#000000", font=('標楷體', 30, 'bold'))
txt.pack(side='top', pady=5)

Button(window, text='擲骰子', bg="#e5ff00", fg='#ff0000', font=(
    '標楷體', 30, 'bold'), command=refresh_screen).pack(side='bottom', pady=10)

var = StringVar(value="6面")
array = ("4面", "6面", "8面", "10面", "12面", "20面")
for index in range(len(array)):
    Radiobutton(window, variable=var,
                value=array[index], text=array[index], font=("標楷體", 16, "bold")).pack(side='left', padx=15)

window.mainloop()
