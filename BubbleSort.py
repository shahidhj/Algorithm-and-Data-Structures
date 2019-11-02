A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def BubbleSort(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

print(BubbleSort(A))