"""
這是十二生肖模組
本模組用於計算十二生肖。
"""

zodiac = '鼠牛虎兔龍蛇馬羊猴雞狗豬'     # 十二生肖
base_year = 2020                       # 鼠年
register = None                        # 年份暫存器


def calculate_zodiac(x):
    """ 計算生肖 """

    global register
    register = x - base_year
    register %= len(zodiac)
    return zodiac[register] + '年'


if __name__ == '__main__':
    print(calculate_zodiac(2020))
    print(calculate_zodiac(2003))
    print(calculate_zodiac(2004))
    print(calculate_zodiac(2024))
    print(calculate_zodiac(2025))
    print(calculate_zodiac(1912))
