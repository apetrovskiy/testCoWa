def narcissistic(value):
    # Code away
    number = str(value)
    number_length = len(number)
    return int(value) == sum([int(x) ** number_length for x in number])


if __name__ == "__main__":
    narcissistic(7)
    narcissistic(371)
    narcissistic(122)
    narcissistic(4887)
