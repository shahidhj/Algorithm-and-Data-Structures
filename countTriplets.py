#Given an array of integers you have to find three numbers such that sum of two elements equals the third element.

A = [5,32,1,7,10,50,19,21,2]


def countTriplets(A):
    i = len(A) - 1
    A.sort()

    while(i >= 0):
        j=0
        k=i-1
        while(j < k):
            if A[j] + A[k] == A[i]:
                return "Pair found and numbers are",A[i],A[j],A[k]
            elif A[j] + A[k] < A[i]:
                j+=1
            else:
                k-=1
        i-=1
print(countTriplets(A))


