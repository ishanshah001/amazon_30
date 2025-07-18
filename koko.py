def minEatingSpeed(piles, h):
    l, r = 1, max(piles) # go through all speeds from 1 to max
    ans = r

    while l <= r:
        mid = (l + r) // 2
        hours = sum((p + mid - 1) // mid for p in piles)

        if hours <= h: #too fast
            ans = mid
            r = mid - 1
        else:
            l = mid + 1 #too slow

    return ans