from typing import List


def pyramid(n):
    result: List[List[int]] = []
    if n == 0:
        return result
    for i in range(n):
        result.append([1 for x in range(i + 1)])
    return result
