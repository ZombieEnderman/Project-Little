"""
這是天干地支模組!\n
本模組用於計算天干地支年份。\n
"""

heavenly_stems = '甲乙丙丁戊己庚辛壬癸'          #天干字串
earthly_branches = '子丑寅卯辰巳午未申酉戌亥'    #地支字串
year_base = 1984                                #基準年(甲子年)

def calculate_HS(year):
    """ 計算天干 """

    year_difference = year - year_base
    return heavenly_stems[year_difference % len(heavenly_stems)]


def calculate_EB(year):
    """ 計算地支 """

    year_difference = year - year_base
    return earthly_branches[year_difference % len(earthly_branches)]