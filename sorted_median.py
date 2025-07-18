def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2) +1
    low, high = 0, len(nums1)
    
    while low <= high:
        i = (low + high) // 2
        j = (total//2) - i
        
        maxX = float('-inf') if i == 0 else nums1[i - 1]
        maxY = float('-inf') if j == 0 else nums2[j - 1]
        minX = float('inf') if i == len(nums1) else nums1[i]
        minY = float('inf') if j == len(nums2) else nums2[j]
        
        if maxX <= minY and maxY <= minX:
            if (total-1) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = i - 1
        else:
            low = i + 1