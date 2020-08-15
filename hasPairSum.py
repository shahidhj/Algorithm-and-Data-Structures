

def hasPairSum(array1,sum):
    for i in range(len(array1)):
        for j in range(i+1,len(array1)):
            if array1[i] + array1[j] == sum:
                return True
    return False

def hasPairSumBetter(array1,sums):
    B = {}
    for eachItem in array1:
        compliment = sums-eachItem
        if eachItem not in B.keys():
            B[compliment] = 1
        else:
            return True
    return False

z = hasPairSumBetter([6,4,3,2,1,7],9)
print(z)