
A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def MergeSort(A):

    if len(A)>1:
        middle = len(A)//2
        left = A[:middle]
        right = A[middle:]


        MergeSort(left),MergeSort(right)

        leftIndex =0
        rightIndex =0
        k=0

        while(leftIndex < len(left) and rightIndex < len(right)):
            if left[leftIndex] < right[rightIndex]:
                A[k]= left[leftIndex]
                leftIndex+=1
            else:
                A[k]=right[rightIndex]
                rightIndex+=1
            k+=1

        while leftIndex < len(left):
            A[k] = (left[leftIndex])
            leftIndex+=1
            k+=1

        while rightIndex < len(right):
            A[k]=(right[rightIndex])
            rightIndex +=1
            k+=1

        return A

def mergeSort(A):
    if len(A)>1:

        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        print("left", left)
        print("right", right)
        print("Before sort A")

        mergeSort(left)
        mergeSort(right)

        leftIndex = 0
        rightIndex =0
        currentIndex =0
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                A[currentIndex] = left[leftIndex]
                leftIndex+=1
            else:
                A[currentIndex] = right[rightIndex]
                rightIndex+=1
            currentIndex+=1

        print("Left iteration",left)
        print("right iteration",right)
        print("Current A",A)

        while leftIndex < len(left):
            A[currentIndex] = left[leftIndex]
            leftIndex+=1
            currentIndex+=1

        while rightIndex < len(right):
            A[currentIndex] = right[rightIndex]
            rightIndex+=1
            currentIndex+=1

        print(A)

print(mergeSort(A))

































print(MergeSort(A))