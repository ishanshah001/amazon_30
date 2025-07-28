from typing import List

class Solution:
    def maxBooksCollected(self, books: List[int]) -> int:
        n = len(books)
        # Adjusted values: makes "decreasing by 1" rule easier to handle
        adjusted = [books[i] - i for i in range(n)]
        
        # Step 1: Find left boundaries using a monotonic stack
        left_bound = [-1] * n
        stack = []
        for i, val in enumerate(adjusted):
            while stack and adjusted[stack[-1]] >= val:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        
        # Step 2: DP to compute max books
        dp = [0] * n
        max_books = 0
        
        for i in range(n):
            # Max number of books we can take at i (limited by slope & left bound)
            length = min(books[i], i - left_bound[i])
            
            first = books[i] - length + 1 #first book in the series
            
            # Sum of decreasing stack: arithmetic series
            # (1 + 100)//2 * 50
            segment_sum = (first + books[i]) * length // 2
            
            # Combine with best from left side if it exists
            dp[i] = segment_sum if left_bound[i] == -1 else segment_sum + dp[left_bound[i]]
            max_books = max(max_books, dp[i])
        
        return max_books

sol = Solution()
print(sol.maxBooksCollected([1, 2, 7, 5, 6]))
print(sol.maxBooksCollected([7,0,3,4,5]))
print(sol.maxBooksCollected([8,2,3,7,3,4,0,1,4,3]))