def same_structure_as(original, other):
    # your code here
    if type(original) is list and type(other) is not list:
        return False
    if type(original) is not list and type(other) is list:
        return False
    if len(original) == 0 and len(other) == 0:
        return True
    if len(original) != len(other):
        return False
    for i in range(0, len(original)):
        if type(original[i]) is list:
            return same_structure_as(original[i], other[i])
    return True
