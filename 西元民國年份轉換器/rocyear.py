"""
這是民國年份模組!
本模組用於計算西元與民國年份。
計算公式:
    民國年份=西元年份-1912+1
    西元年份=民國年份+1912-1
變數:
    1.roc_first_year可獲取民國元年之西元年份
"""

roc_first_year=1912     #民國元年

def roc_year(x=1912):
    """ 將西元年份轉換成民國年份 """

    difference_year=x - roc_first_year + 1      #年份差
    return difference_year


def ad_year(x):
    """ 將民國年份轉換成西元年份 """

    difference_year=x + roc_first_year - 1      #年份差
    return difference_year