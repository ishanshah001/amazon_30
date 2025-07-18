def twoSum(nums, target):
    dict = {}
    for index, item in enumerate(nums):
        if item in dict:
            return [dict[item], index]
        diff = target - item
        dict[diff] = index