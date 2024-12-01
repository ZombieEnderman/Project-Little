"""
這是檔案下載速率計算器主系統!
本系統用於整合其他附屬模組。
※公式如下:
    下載時間 = 檔案大小 X 8 ÷ 傳輸速率
※傳輸速率差距為1,000、檔案大小差距為1,024
"""

# 模組區
from tkinter import *

# 系統區
file=int(input('file:'))
mb=file * 1_024 * 1_024 * 8
mbps=1_000 * 1_000
print(round(mb/mbps,2))