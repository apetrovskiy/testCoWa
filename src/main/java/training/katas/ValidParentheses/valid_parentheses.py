def valid_parentheses(string):
    # your code here
    if string.count('(') == 0 and string.count(')') == 0:
        return True
    if string.count('(') != string.count(')'):
        return False
    left_brackets_number = 0
    right_brackets_number = 0
    while len(string) > 0:
        left_bracket_position = string.find('(')
        right_bracket_position = string.find(')')
        if left_bracket_position < right_bracket_position and left_bracket_position != -1:
            left_brackets_number += 1
            string = string[left_bracket_position + 1:]
        if left_bracket_position > right_bracket_position and right_bracket_position != -1:
            right_brackets_number += 1
            string = string[right_bracket_position + 1:]
        if left_bracket_position == -1:
            right_brackets_number += 1
            string = string[right_bracket_position + 1:]
        if right_bracket_position == -1:
            left_brackets_number += 1
            string = string[left_bracket_position + 1:]
        if right_brackets_number > left_brackets_number:
            return False
        if len(string) == 0 or (left_bracket_position == -1 and right_bracket_position == -1):
            return True
    return True
