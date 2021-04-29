def iq_test(numbers):
    # your code here
    selection = [x % 2 for x in range(0, 3)]
    search_for_even: bool = False if selection.count(
        0) > selection.count(1) else True
    for i in range(len(numbers)):
        if search_for_even:
            if numbers[i] % 2 == 0:
                return i+1
        else:
            if numbers[i] % 2 == 1:
                return i+1
    return 0
