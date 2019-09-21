#Reverse a string in python


A= "MyNameIsShahid"
print(A[::-1])
Strings=""

for i in range(len(A)-1,-1,-1):
    Strings = Strings +A[i]

print(Strings)