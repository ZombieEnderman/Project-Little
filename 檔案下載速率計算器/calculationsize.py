"""
這是計算大小模組!\n
本模組用於計算檔案大小、傳輸速率、時間。\n
"""

file_size=None  #檔案大小暫存器
velocity=None   #傳輸速率暫存器
time=None       #時間暫存器

capacity={'KB':2 ** 13,
          'MB':2 ** 23,
          'GB':2 ** 33,
          'TB':2 ** 43,
          'PB':2 ** 53,
          'EB':2 ** 63,
          'ZB':2 ** 73}           #檔案大小字典

transmission={'Kbps':10 ** 3,
              'Mbps':10 ** 6,
              'Gbps':10 ** 9,
              'Tbps':10 ** 12,
              'Pbps':10 ** 15,
              'Ebps':10 ** 18,
              'Zbps':10 ** 21}    #傳輸速率字典

def calculate_size(unit,value):
    """ 計算檔案大小 """

    global file_size
    file_size = capacity[unit] * value


def calculate_speed(unit,value):
    """ 計算傳輸速率 """

    global velocity
    velocity = transmission[unit] * value


def calculate_time(second):
    """ 計算時間 """

    global time
    if second >= 3_600:
        hour = int(second // 3_600)
        minute = int((second % 3_600) // 60)
        second %= 60
        time = (hour,minute,round(second,2))
    elif 60 <= second < 3_600:
        minute = int(second // 60)
        second %= 60
        time = (0,minute,round(second,2))
    else:
        time = (0,0,round(second,2))