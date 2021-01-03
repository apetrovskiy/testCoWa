EMPTY = ''


def solution_roman_numerals_encoder(n):
    # TODO convert int to roman string
    return build_thousands(n) + build_hundreds(n) + build_tens(n) + build_ones(n)


def build_thousands(n: int) -> str:
    if n < 1000:
        return EMPTY
    thousands = int(str(n)[-4:-3])
    return build_roman_string(thousands, 'M', '', '')


def build_hundreds(n: int) -> str:
    if n < 100:
        return EMPTY
    thousands = int(str(n)[-3:-2])
    return build_roman_string(thousands, 'C', 'D', 'M')


def build_tens(n: int) -> str:
    if n < 10:
        return EMPTY
    thousands = int(str(n)[-2:-1])
    return build_roman_string(thousands, 'X', 'L', 'C')


def build_ones(n: int) -> str:
    thousands = int(str(n)[-1:])
    return build_roman_string(thousands, 'I', 'V', 'X')


def build_roman_string(n: int, one_char: str, five_char: str, ten_char: str) -> str:
    print(n)
    switcher = {
        0: EMPTY,
        1: one_char,
        2: one_char + one_char,
        3: one_char + one_char + one_char,
        4: one_char + five_char,
        5: five_char,
        6: five_char + one_char,
        7: five_char + one_char + one_char,
        8: five_char + one_char + one_char + one_char,
        9: one_char + ten_char
    }
    return switcher.get(n, "Invalid value")
