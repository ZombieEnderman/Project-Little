"""
這是BMI計算模組!
本模組用於計算BMI。
BMI計算公式:
    BMI=體重/身高**2(公尺)
變數:
    1.bmi_norm取得BMI標準指數的字典
"""

bmi_norm={'BMI < 18.5':'過輕',
          '18.5 <= BMI < 24':'正常',
          '24 <= BMI < 27':'過重',
          '27 <= BMI < 30':'輕度肥胖',
          '30 <= BMI < 35':'中度肥胖',
          '35 <= BMI':'重度肥胖'}


def bmi_compute(kg,m):
    """ 計算BMI """

    body_weight=kg
    body_height=m ** 2
    bmi=body_weight / body_height
    return bmi


def isNormal(bmi):
    """ 判斷BMI是否為正常值 """

    if 18.5 <= bmi < 24:
        return True
    return False


def isLight(bmi):
    """ 判斷BMI是否過輕 """

    if bmi < 18.5:
        return True
    return False


def isHeavy(bmi):
    """ 判斷BMI是否過重 """

    if 24 <= bmi < 27:
        return True
    return False


def isFat(bmi):
    """ 判斷BMI是否為輕度肥胖值 """

    if 27 <= bmi < 30:
        return True
    return False


def isObesity(bmi):
    """ 判斷BMI是否為中度肥胖值 """

    if 30 <= bmi < 35:
        return True
    return False


def isOver(bmi):
    """ 判斷BMI是否為重度肥胖值 """

    if 35 <= bmi:
        return True
    return False