#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words

def permutationPalindrome(word):
    characterHash = {}
    foundOdd = False
    for i in range(len(word)):
        if word[i] not in characterHash:
            characterHash[word[i]] = 1
        else:
            characterHash[word[i]] +=1

    for characters in characterHash:
        if characterHash[characters] % 2 == 1:
            if(foundOdd):
                return False
            foundOdd = True
    return True



print(permutationPalindrome("racecar "))
