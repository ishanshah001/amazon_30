from typing import List

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # Find leftmost minimum and rightmost maximum positions
        min_position = min(range(len(nums)), key=lambda i: (nums[i], i))
        max_position = max(range(len(nums)), key=lambda i: (nums[i], -i))
        
        # Swaps to bring min to front + max to end
        swaps = min_position + (len(nums) - 1 - max_position)
        
        # Adjust if min is after max (one swap overlaps)
        if min_position > max_position:
            swaps -= 1
            
        return swaps
