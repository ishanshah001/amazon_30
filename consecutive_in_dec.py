class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left = [0]*len(security)
        right = [0]*len(security)
        for i in range(1, len(security)):
            if security[i]<=security[i-1]:
                left[i] = left[i-1]+1
        for i in range(len(security)-2, -1, -1):
            if security[i]<=security[i+1]:
                right[i] = right[i+1]+1
        count = []
        for i in range(time, len(security)-time):
            if left[i]>=time and right[i]>=time:
                count.append(i)
        return count