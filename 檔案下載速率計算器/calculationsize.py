"""
這是計算大小模組!\n
本模組用於計算檔案大小、傳輸速率、時間。\n
"""

file_size=None  #檔案大小暫存器
velocity=None   #傳輸速率暫存器
time=None       #時間暫存器

capacity={'KB':pow(2,13),
          'MB':pow(2,23),
          'GB':pow(2,33),
          'TB':pow(2,43),
          'PB':pow(2,53),
          'EB':pow(2,63),
          'ZB':pow(2,73)}           #檔案大小字典

transmission={'Kbps':pow(10,3),
              'Mbps':pow(10,6),
              'Gbps':pow(10,9),
              'Tbps':pow(10,12),
              'Pbps':pow(10,15),
              'Ebps':pow(10,18),
              'Zbps':pow(10,21)}    #傳輸速率字典

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
        hour = second // 3_600
        minute = second % 3_600
        second = minute % 60
        time = (hour,minute,second)
    elif 60 <= second < 3_600:
        minute = second // 60
        second %= 60
        time = (0,minute,second)
    else:
        time = (0,0,second)