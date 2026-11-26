class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        minheap = []
        
        for stick in sticks:
            heapq.heappush(minheap,stick)

        total = 0

        while len(minheap)>1:
            first = heapq.heappop(minheap)
            second = heapq.heappop(minheap)


            cost = first+second

            total+=cost

            heapq.heappush(minheap,cost)

        return total


















        