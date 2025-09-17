"""
這是骰子模組!\n
本模組用於生成亂數。\n
"""

from random import randint as scope


def four_sides(n: int = 1) -> tuple[int, ...]:
    """生成n個範圍1~4的數字"""
    return tuple(scope(1, 4) for _ in range(n))


def six_sides(n: int = 1) -> tuple[int, ...]:
    """生成n個範圍1~6的數字"""
    return tuple(scope(1, 6) for _ in range(n))


def eight_sides(n: int = 1) -> tuple[int, ...]:
    """生成n個範圍1~8的數字"""
    return tuple(scope(1, 8) for _ in range(n))


def ten_sides(n: int = 1) -> tuple[int, ...]:
    """生成n個範圍1~10的數字"""
    return tuple(scope(1, 10) for _ in range(n))


def twelve_sides(n: int = 1) -> tuple[int, ...]:
    """生成n個範圍1~12的數字"""
    return tuple(scope(1, 12) for _ in range(n))


def twenty_sides(n=1) -> tuple[int, ...]:
    """生成n個範圍1~20的數字"""
    return tuple(scope(1, 12) for _ in range(n))


if __name__ == "__main__":
    print(four_sides(2))
    print(six_sides(3))
    print(eight_sides(4))
    print(ten_sides(5))
    print(twelve_sides(6))
    print(twenty_sides(10))
