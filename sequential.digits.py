from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int):
        
        res = []
        queue = deque(range(1,10))

        while queue:
            num = queue.popleft()
            if low <= num <= high:
                res.append(num)
            elif num>high:
                break
            last = num%10
            if last < 9:
                queue.append(num*10 + last +1)
        return res