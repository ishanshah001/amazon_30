from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, times: list[int], costs: list[int], budget: int) -> int:
        n = len(times)
        left = 0                   # left pointer of window
        total_running = 0          # sum of running costs in current window
        charge_values = SortedList()  # sorted charge times in current window
        max_len = 0

        for right in range(n):
            # 1. Expand the window by adding the new robot
            total_running += costs[right]
            charge_values.add(times[right])

            # 2. Shrink window if cost exceeds budget
            if charge_values[-1] + (right - left + 1) * total_running > budget:
                charge_values.remove(times[left])
                total_running -= costs[left]
                left += 1

            # 3. Update max length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len
