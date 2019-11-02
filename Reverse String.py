#Reverse a string in python


A= "MyNameIsShahid"
print(A[::-1])
Strings=""

for i in range(len(A)-1,-1,-1):
    Strings = Strings +A[i]

print(Strings)

def ReverseRecursive(A):
    if len(A) ==0 :
        return A
    else:
        return ReverseRecursive(A[1:]) + A[0]

B=ReverseRecursive("shahid")
print("Reversed String ", B)