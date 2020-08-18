def longestWord(word):
    word_list = word.split(" ")
    biggestWord = ""
    for word in word_list:
        if len(word) > len(biggestWord):
            biggestWord = word
    return biggestWord

print(longestWord("I love Dogs"))
