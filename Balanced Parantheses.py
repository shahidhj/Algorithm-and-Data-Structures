def hasBalancedParentheses(charArray):
    S=[]
    for char in charArray:
        if char =="{" or char =="(" or char =="[":
            S.append(char)
            continue
        if(len(S) ==0):
            return False
        elif(char == ")"):
            x = S.pop()
            if(x == "{" or x =="["):
                return False
        elif(char == "]"):
            x=S.pop()
            if (x == "{" or x == "("):
                return False
        elif (char == "}"):
            x = S.pop()
            if (x == "[" or x == "("):
                return False
    if len(S):
        return False
    else:
        return True

if(hasBalancedParentheses("{[()]}")):
    print("Balanced")
else:
    print("unbalanced")