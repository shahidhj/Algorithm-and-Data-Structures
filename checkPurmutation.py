# Given two strings check if one string is permutation of another

def permutationString(str1,str2):
    str1Sum=0
    str2Sum=0
    if len(str1) != len(str2):
        return False

    for char in str1.lower():
        str1Sum+=ord(char)

    for char in str2.lower():
        str2Sum+=ord(char)

    if str1Sum == str2Sum:
        return True

    return False

print(permutationString("doG","god"))


