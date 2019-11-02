A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

def SelectionSort(A):
    for i in range(0,len(A)):
        min_indx = i
        for j in range(i+1,len(A)):
            if A[min_indx] > A[j]:
                 min_indx = j
        A[i],A[min_indx]= A[min_indx],A[i]
    return A

print(SelectionSort(A))