# import heapq
# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
#         dist = [0]*len(nums)
#         heapq.heapify(dist)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 heapq.heappush(dist, abs(nums[i]-nums[j]))

#         while k!=1:
#             heapq.heappop(dist)
#             k-=1
#         return heapq.heappop(dist)

class Solution:
    def getPairs(self, t, nums):
        cnt = 0
        l = 0
        for r in range(1, len(nums)):
            while l < r and t < nums[r] - nums[l]:
                l += 1
            cnt += r - l
        return cnt
    
    def smallestDistancePair(self, nums, k):
        nums.sort()
        l, r = 0, nums[-1]
        while l < r:
            mid = (l + r) // 2
            if self.getPairs(mid, nums) < k:
                l = mid + 1
            else:
                r = mid
        return l