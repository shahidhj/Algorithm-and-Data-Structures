# Program to merge two sorted arrays


def checkForNullArray(Array1,Array2):
    if len(Array1) < 1:
        return Array2
    elif len(Array2) <1 :
        return Array1


def MergeSortedArray(Array1,Array2):
    i=0
    j=0
    MergeArray = []
    #Array1Item = Array1[0]Array1 =[3,4,6,7,10,15]
    #Array2 = [1,2,8,14,16]
    #Array2Item = Array2[0]
    checkForNullArray(Array1,Array2)
    while i < len(Array1) and j < len(Array2) :
        if Array1[i] < Array2[j] :
            MergeArray.append(Array1[i])
            i+=1
        else:
            MergeArray.append(Array2[j])
            j+=1

    while j <len(Array2):
        MergeArray.append((Array2[j]))
        j+=1

    while i < len(Array1):
        MergeArray.append(Array1[i])
        i+=1
    print(MergeArray)

Array1 =[3,4,6]
Array2 = [1,2,8,14,16]
MergeSortedArray(Array1,Array2)