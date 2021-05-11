R = 'R'
G = 'G'
B = 'B'


def get_color(color1: str, color2: str) -> str:
    if color1 == color2:
        return color1
    else:
        return R if color1 != R and color2 != R \
            else (G if color1 != G and color2 != G else B)


# TODO: optimize it
def triangle(row):
    result = row
    while len(result) > 1 and result != "":
        current_row = result
        result = ""
        for i in range(len(current_row)-1):
            result += get_color(current_row[i], current_row[i+1])
    return result
