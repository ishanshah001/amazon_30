class Solution:
    def trap(self, heights):
        max_left = [0] * len(heights)
        max_right =[0] * len(heights)
        for i in range(1, len(heights)):
            max_left[i] = max(heights[i-1], max_left[i-1])
        for i in range(len(heights)-2, -1, -1):
            max_right[i] = max(heights[i+1], max_right[i+1])
        total = sum([max(0,min(max_left[i],max_right[i])-heights[i]) for i in range(len(heights))])
        return total
        