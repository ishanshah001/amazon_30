class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1]) #returns index of first occurence of the last char
            if i == len(s) - 1:
                res += i // 2 #If it's already at the end: it’s the middle character → takes fewer swaps.
            else:
                res += i #num of swaps equals those many times to the left
                s.pop(i)
            s.pop()
        return res