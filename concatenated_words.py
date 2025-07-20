class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if (prefix in words) and (suffix in words or dfs(suffix)):
                    dp[word] = True
                    return True
            dp[word] = False

        for i in words:
            if dfs(i):
                res.append(i)
        return res
