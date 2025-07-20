class Solution:
    def minSwaps(self, s: str) -> int:
        count_0 = s.count("0")
        count_1 = len(s) - count_0
        if abs(count_0 - count_1) > 1:
            return -1
        max_char = "0" if count_1 < count_0 else count_0
        sum_zero = 0
        sum_one = 0
        for i in range(len(s)):
            if int(s[i])==i%2:
                sum_one+=1
            else:
                sum_zero+=1
        
        if count_0 == count_1:
            return min(sum_one//2, sum_zero//2)
        if max_char == "0":
            return sum_zero//2
        return sum_one//2