# find if all characters in a string are unique

def uniqueCharacters(A):
    characterHash = {}
    for i in range(len(A)):
        if A[i] in characterHash:
            return False
        else:
            characterHash[A[i]] = 1
    print(characterHash)
    return True

print(uniqueCharacters("shahid"))
