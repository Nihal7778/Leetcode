class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxheap = []
      

        for x,y in points:
            dist = x**2 + y**2

            heapq.heappush(maxheap,(-dist,x,y))

            if len(maxheap)>k:
                heapq.heappop(maxheap)

        result = []
        while maxheap:
            distance,x,y  = heapq.heappop(maxheap)
            result.append([x,y])
        
        return result


