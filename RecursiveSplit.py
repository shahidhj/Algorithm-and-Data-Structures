
A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def RecursiveSplit(A):

    if len(A)>1:
        middle = len(A)//2
        left = A[:middle]
        right = A[middle:]


        RecursiveSplit(left),RecursiveSplit(right)
        