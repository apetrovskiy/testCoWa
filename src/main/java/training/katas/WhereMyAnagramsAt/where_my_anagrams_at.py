def anagrams(word, words):
    # your code here
    result = []
    if len(word) == 0 or len(words) == 0:
        return result
    sorted_word = sorted(word)
    for i in range(len(words)):
        if sorted_word == sorted(words[i]):
            result.append(words[i])
    return result
