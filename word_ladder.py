from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        neighbors = {}
        for word in wordList:
            for c in range(len(word)):
                key = word[0:c]+"*"+word[c+1:len(word)]
                if key in neighbors:
                    neighbors[key].append(word)
                else:
                    neighbors[key] = [word]
        path = {}
        queue = deque([beginWord])
        path[beginWord] = None
        visited = set()
        found = False
        while queue and not found:
            word = queue.popleft()
            if word not in visited:
                visited.add(word)
                n = []
                for c in range(len(word)):
                    key = word[0:c]+"*"+word[c+1:len(word)]
                    n=n+neighbors[key] if key in neighbors else n
                for neighbor in n:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        path[neighbor] = word
                        if neighbor == endWord:
                            found = True
                            break
        count = 0
        if found:
            curr = endWord
            while curr!=None:
                curr = path[curr]
                count+=1
        print(path)
        return count