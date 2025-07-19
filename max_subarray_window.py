from collections import deque
def maxSlidingWindow(self, nums, k):
    res = []
    q = deque()
    l=r=0
    while r<len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # since decreasing, if current l is greater than q, that val is out of consideration
        if l>q[0]:
            q.popleft()
        
        # once we reach size k, left most will always be max value
        if (r+1)>=k:
            res.append(nums[q[0]])
            l+=1
        r+=1
    return res
            
            