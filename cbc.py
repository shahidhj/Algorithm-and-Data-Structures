
T = ['test1a','test2','test1b','test3','test4a','test4b']
R = ['Wrong answer', 'OKa', 'Runtime error','OK','OK','OK']

def solution(T,R):
    count = 0
    subGroupdsHash = {}
    for t,r in zip(T,R):
        if t[-1].isdigit():
            if r == "OK":
                subGroupdsHash[t[-1]] = r
                count+=1
        else:
            z = str(t[-2])
            if z not in subGroupdsHash.keys():
                subGroupdsHash[z] = [r]
            else:
                subGroupdsHash[z].append(r)


    for key,values in subGroupdsHash.items():
        check = True
        result = all(value == "OK" for value in values)
        if result == True:
            count+=1
    answer = round((count * 100) / len(subGroupdsHash))
    print(answer)


    print(subGroupdsHash)
    print(count)
    print(len(subGroupdsHash))

solution(T,R)