class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        OPTIMIZATION:
        Since we only need last_seen and sec_last_seen, we need 2d array with second dimension with len=2. 
        For dp table, we only refer to dp[i-1], so we can just use a simple counter
        Time: O(n)
        Space: O(26 * 2) = O(n)
        """
        # last_seens[-1] is previous seen, last_seens[-2] is sec previous seen.
        last_seens = [[-1, -1] for _ in range(26)]
        unique_count = 0
        dp = 0

        for i, c in enumerate(s):
            idx = ord(c) - ord('A')
            dp_new = dp + (i - last_seens[idx][-1]) - (last_seens[idx][-1] - last_seens[idx][-2])
            last_seens[idx] = [last_seens[idx][-1], i]
            dp = dp_new
            unique_count += dp
            print(dp)

        return unique_count