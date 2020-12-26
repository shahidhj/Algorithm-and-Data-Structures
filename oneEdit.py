#One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.

def oneEdit(str1,str2):
    if len(str1) == len(str2):
        return oneEditReplace(str1,str2)



def oneEditReplace(str1,str2):
    foundDifference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundDifference:
                return False
        foundDifference = True

    return True

