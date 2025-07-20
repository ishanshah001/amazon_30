class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        query_count = []
        right_min = [-1]*len(s)
        left_min = [-1]*len(s)
        if s[-1]== "|":
            right_min[-1]=len(s)-1

        if s[0]== "|":
            left_min[0]=0
        
        plates = [0]* len(s)
        count = 0
        for i in range(len(s)):
            if s[i]=="*":
                count+=1
            plates[i]=count

        for i in range(1,len(s)):
            if s[i] == "|":
                left_min[i] = i
            elif left_min[i-1]:
                left_min[i] = left_min[i-1]
        for i in range(len(s)-2, -1,-1):
            if s[i] == "|":
                right_min[i] = i
            elif right_min[i+1]:
                right_min[i] = right_min[i+1]
        
        for low, high in queries:
            left = right_min[low]
            right = left_min[high]
            if left != -1 and right != -1 and left < right:
                query_count.append(plates[right] - plates[left])
            else:
                query_count.append(0)

        return query_count