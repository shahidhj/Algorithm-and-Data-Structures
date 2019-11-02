A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def InsertionSort(A):
    for i in range(1,len(A)):
        currentElement = A[i]
        while(i >0 and A[i-1] > A[i]):
            A[i] = A[i-1]
            i = i -1
            A[i] = currentElement
    return A

print(InsertionSort(A))
