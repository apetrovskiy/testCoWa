from typing import List


def move_zeros(array):
    values: List[int] = []
    zeroes: List[int] = []
    [values.append(x) if x != 0 else zeroes.append(x) for x in array]
    return values + zeroes
