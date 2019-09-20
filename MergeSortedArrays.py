# Program to merge two sorted arrays


def checkForNullArray(Array1,Array2):
    if len(Array1) < 1:
        return Array2
    elif len(Array2) <1 :
        return Array1


def MergeSortedArray(Array1,Array2):
    i=1
    j=1
    MergeArray = []
    Array1Item = Array1[0]
    Array2Item = Array2[0]
    checkForNullArray(Array1,Array2)
    while Array1Item or Array2Item:
        if (Array1Item < Array2Item or Array2Item == None):
            MergeArray.append(Array1Item)
            Array1Item = Array1[i]
            i+=1

        else:
            MergeArray.append(Array2Item)
            Array2Item = Array2[j]
            j+=1

        print(MergeArray)


Array1 = [1,3,5]
Array2 =[3,4,6]
MergeSortedArray(Array1,Array2)