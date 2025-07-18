def canJump(nums):
    if len(nums) == 1:
        return True
    i = 0
    lst = [False for x in nums]
    if not nums[0]:
        return False
    lst[0] = True
    while i<len(nums)-1:
        if not lst[i]:
            return False
        jump = nums[i]
        k = i
        while k<len(nums)-1 and jump>0:
            k+=1
            lst[k] = True
            jump-=1
        i+=1
        if lst[-1]:
            return True
    return False

