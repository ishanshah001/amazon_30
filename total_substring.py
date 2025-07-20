class Solution:
    def appealSum(self, s: str) -> int:
        visited = {}
        total = 0
        for i in range(len(s)):
            if s[i] not in visited:
                sum = (i+1)*(len(s)-i)
            else:
                sum = (i-visited[s[i]])*(len(s)-i)
            visited[s[i]] = i
            total+=sum
        return total