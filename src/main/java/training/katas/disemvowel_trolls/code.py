VOWELS = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]


def disemvowel(string):
    return "".join([x for x in string if x not in VOWELS])
