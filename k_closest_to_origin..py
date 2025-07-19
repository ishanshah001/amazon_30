import heapq as hq

class Solution:
    def kClosest(self, points, k):
        distance = []

        for i in range(len(points)):
            dist = sqrt(points[i][0]**2+points[i][1]**2)
            distance.append((dist, points[i]))
        hq.heapify(distance)
        lst = []
        for i in range(k):
            lst.append(hq.heappop(distance)[1])
        return lst