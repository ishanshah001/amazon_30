class Solution:
    def minimumOperations(nums):
        lst = []
        for i in nums:
            if i!=0:
                lst.append(i)
        return len(set(lst))