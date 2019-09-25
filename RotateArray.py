def RotateArray(Array1,k):
    newArray=[]
    newArray= Array1[k+1::]+Array1[:k+1]
    print(newArray)

RotateArray([1,2,3,4,5,6,7],3)