class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        while(l!=len(nums)-1):
            if nums[l]==0:
                r=l+1
                while r!=len(nums) and nums[r]==0:
                    r+=1
                if r==len(nums):
                    break
                nums[l], nums[r] = nums[r], nums[l]
            l+=1
            