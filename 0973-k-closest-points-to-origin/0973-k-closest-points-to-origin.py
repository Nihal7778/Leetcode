class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []

        for x, y in points:
            dist = x**2+y**2

            heapq.heappush(maxHeap,(-dist,x,y))

            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        result = []

        for dist,x,y in maxHeap:
            result.append([x,y])

        return result
        