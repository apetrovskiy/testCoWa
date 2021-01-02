EXES = ['x', 'X']
OHS = ['o', 'O']


def xo(s: str):
    # return True
    return len([x for x in s if x in EXES]) == len([x for x in s if x in OHS])
