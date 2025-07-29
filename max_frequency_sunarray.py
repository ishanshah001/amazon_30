class Solution:
    def maxFrequency(self, nums, k):
        base = nums.count(k)
        max_gain = 0

        for target in set(nums):
            if target == k: 
                continue
            current = best = 0
            for num in nums:
                if num == target: 
                    current += 1
                elif num == k:    
                    current -= 1
                current = max(current, 0) #reset to 0
                best = max(best, current)
            max_gain = max(max_gain, best)

        return base + max_gain