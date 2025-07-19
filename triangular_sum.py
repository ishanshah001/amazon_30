def triangularSum(self, nums):
    prev = nums
    for i in range(len(nums)-1):
        sum = []
        for j in range (len(prev)-1):
            sum.append((prev[j]+prev[j+1])%10)
        prev = sum
    return prev[0]