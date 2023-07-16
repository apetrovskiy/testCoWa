def find_it(seq):
    # return None
    dict_value_to_count = [
        {x: len([y for y in seq if y == x])}
        for x in seq
        if len([y for y in seq if y == x]) % 2 != 0
    ]
    val = [x for dict in dict_value_to_count for x in dict.values()][0]
    return [x for dict in dict_value_to_count for x in dict.keys() if dict[x] == val][0]
