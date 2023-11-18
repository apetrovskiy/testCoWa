def row_sum_odd_numbers(n):
    max_num = n * (n + 1) - 1
    result: int = 0
    for i in range(max_num, max_num - n * 2, -2):
        result += i
    return result
