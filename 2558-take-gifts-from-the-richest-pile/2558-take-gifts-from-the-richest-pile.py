class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = [-gift for gift in gifts]

        heapq.heapify(maxheap)

        for i in range(k):
            largest = -maxheap[0]

            if largest == 1:
                break

            remaining = math.isqrt(largest)

            heapq.heapreplace(maxheap,-remaining)


        return -sum(maxheap)


        # t.c - O(n+klogn)
        # s.c - O(n)




