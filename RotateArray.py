def RotateArray(A,K):
    newArray=[]
    newArray= A[-K::] + A[:-K:]
    print(newArray)

RotateArray([-1,-100,3,99],2)