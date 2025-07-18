def productExceptSelf(self, nums):
    left = [nums[0]]
    right = [nums[-1]]
    prod = []
    for i in range(1, len(nums)):
        left.append(left[i-1]*nums[i])
    for i in range(1, len(nums)):
        right.insert(0, nums[-1*i-1]*right[0])
    for i in range(len(nums)):
        if i == 0:
            prod.append(right[i+1])
        elif i == len(nums)-1:
            prod.append(left[i-1])
        else:
            prod.append(left[i-1]*right[i+1])
    return prod