import heapq as hq
import re
from collections import deque
class Solution:
    def reorderLogFiles(self, logs):
        letter = []
        digit = deque()
        pattern = r".*\d.*"
        for i in range(len(logs)):
            id, log = logs[i].split(" ", 1)
            
            if re.search(r"\d", log):
                print(log)
                digit.append(logs[i])
            else:
                hq.heappush(letter, (log, logs[i]))
         
        op = []

        while letter:
            op.append(hq.heappop(letter)[1])
        while digit:
            op.append(digit.popleft())
        return op