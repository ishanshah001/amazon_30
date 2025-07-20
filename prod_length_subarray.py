
# keeping track of last encountered positive and negative product

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, ans = 0,0,0
        for n in nums:
            if n>0:
                pos+=1 #increase last encountered pos prod by
                neg= 1+neg if neg else 0 #increment only if found a neg number
            elif n<0:
                pos, neg = 1+neg if neg else 0, 1+pos #since a negative is found, places are swapped
            else:
                pos, neg = 0,0
            ans = max(ans, pos)
        return ans
            
            