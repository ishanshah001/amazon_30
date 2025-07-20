import heapq

class Solution:
    def kSum(self, nums, k):
        maxSum = sum(num for num in nums if num > 0)
        absNums = sorted(abs(num) for num in nums)
        n = len(absNums)

        minHeap = [(absNums[0], 0)]
        removedSums = [0]  # delta = 0 means we keep all positive elements

        while len(removedSums) < k:
            currSum, i = heapq.heappop(minHeap)
            removedSums.append(currSum)

            if i + 1 < n:
                # include next element in removal
                heapq.heappush(minHeap, (currSum + absNums[i+1], i + 1))
                # replace current with next
                heapq.heappush(minHeap, (currSum - absNums[i] + absNums[i+1], i + 1))

        return maxSum - removedSums[k-1]
    

# kth largest sum is same as kth smallest diff from largest sum

# absolute values. store currsum and index in heap. for every node, add i+1 or replace current one with i+1