import heapq

class Solution:
    def arraySum(self, nums):
        # maxSum = sum(num for num in nums if num > 0)
        # absNums = sorted(abs(num) for num in nums)
        n = len(nums)

        minHeap = [(nums[0], 0)]
        removedSums = [0]  # delta = 0 means we keep all positive elements

        # while len(removedSums) < k:
        while minHeap:
            currSum, i = heapq.heappop(minHeap)
            removedSums.append(currSum)

            if i + 1 < n:
                # include next element in removal
                heapq.heappush(minHeap, (currSum + nums[i+1], i + 1))
                # replace current with next
                heapq.heappush(minHeap, (currSum - nums[i] + nums[i+1], i + 1))
        print(removedSums)
    

Solution().arraySum([1,2,3,4,-5])

# store currsum and index in heap. for every node, add i+1 or replace current one with i+1