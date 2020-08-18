A = [1,2,3,4]

def containsDuplicate(Array1):
    duplicateHash = {}
    for eachElement in A:
        if eachElement not in duplicateHash.keys():
            duplicateHash[eachElement] = 1
        else:
            return True
    return False

C = containsDuplicate(A)
print(C)