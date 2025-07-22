# sum of all subarrays
from itertools import accumulate
class Solution:    
    def totalStrength(self, A):
        mod = 10 ** 9 + 7
        n = len(A)
        
        # next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each A[i] as minimum, calculate sum
        result = 0

        # First prefix tells you: What is the sum of the given array at each index?
        # Second prefix tells you: What is the sum of all those sums at each index (sum of all subarrays from 1 to n)?
        # since its cotinuous array, we want to find sums of all possible subarrays between l and r
        
        prefix_of_prefix = list(accumulate(accumulate(A), initial=0))

        for i in range(n):
            
            left_bound = left[i]
            right_bound = right[i]
            

            # Number of elements to the left and right where A[i] is the minimum
            count_left = i - left_bound
            count_right = right_bound - i

            # Sum of prefix sums on the left and right of i
            sum_left_prefixes = prefix_of_prefix[i] - prefix_of_prefix[max(left_bound, 0)]
            sum_right_prefixes = prefix_of_prefix[right_bound] - prefix_of_prefix[i]

            # Calculate contribution of A[i] across all valid subarrays
            # this is like sum*(n-1) so it doesnt double count
            contribution = A[i] * (sum_right_prefixes * count_left - sum_left_prefixes * count_right)
            result += contribution
        
        return result%mod
