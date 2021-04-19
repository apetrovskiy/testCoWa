def solution(s):
    print(s)
    if len(s) == 0:
        return []
    print([s[index] + (s[index + 1] if index + 1 < len(s) else '_')
           for index in range(0, len(s), 2)])
    return [s[index] + (s[index + 1] if index + 1 < len(s) else '_')
            for index in range(0, len(s), 2)]
