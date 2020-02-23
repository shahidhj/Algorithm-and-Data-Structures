
#Input A=[0,1,0,3,12]
#Output: [1,3,12,0,0]

A=[0,1,0,3,12]
B=[1,3,12,0,0]

zero = 0
for i in range(len(A)):
    if A[i] != 0:
        A[i],A[zero] = A[zero],A[i]
        zero+=1
print(A)
