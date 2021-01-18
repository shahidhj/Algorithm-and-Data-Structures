


def mergreList(originalList,additionList,removalList): # Intial function that performs addition and removal to original list
    uniqueStrings = {} # Hash table to store all the unique elements of the list
    uniqueList = [] # final unsorted list

    for eachString in originalList:
        if eachString not in uniqueStrings.keys():
            uniqueStrings[eachString] = 1

    for eachString in additionList:
        if eachString not in uniqueStrings.keys():
            uniqueStrings[eachString]=1

    for eachString in removalList:
        if eachString in uniqueStrings.keys():
            uniqueStrings.pop(eachString,None)

    for key in uniqueStrings.keys():
        uniqueList.append(key)

    #print(finalList)
    return uniqueList # return the final unsorted list of unique items

def sortResultList():
    resultList = mergreList(['one','two','three'],['one','two','five','six'],['two','five'])
    resultList.sort(key=len,reverse=True) # sorting the finalList based on length of each string

    for i in range(len(resultList)-1,-1,-1): # loop through the list and reverse items alphabetically if they are of same length
        if len(resultList[i]) == len(resultList[i-1]):
            if ord(resultList[i][0]) > ord(resultList[i-1][0]):
                resultList[i],resultList[i-1] = resultList[i-1],resultList[i]

    return resultList

print(sortResultList())


#mergreList(['one','two','three'],['one','two','five','six'],['two','five'])

