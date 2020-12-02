
def longestSubStringWithoutRepeatingCharacters(A):
    maps = {}
    start=max_length=0
    for i in range(len(A)):
        if A[i] in maps and start<= maps[A[i]]:
            start = maps[A[i]] + 1
        else:
            max_length = max(max_length,i-start+1)

        maps[A[i]] = i
    return max_length

print(longestSubStringWithoutRepeatingCharacters("abcdabcabc"))
