import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heap

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1

            else:
                hashmap[num]=1

        minheap = []

        for num,freq in hashmap.items():
            heapq.heappush(minheap,(freq,num))

            if len(minheap)>k:
                freq,num = heapq.heappop(minheap)

        
        result = []

        while minheap:
            freq,num = heapq.heappop(minheap)

            result.append(num)

        return result


        #T.c = O(n + m log k) , s.c = O(m+k)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #optimal
        # hashmap = {}

        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num]+=1

        #     else:
        #         hashmap[num]=1

        # buckets = [[] for _ in range(len(nums)+1)]

        # for num,freq in hashmap.items():
        #     buckets[freq].append(num)

        # result = []

        # for freq in range(len(buckets)-1,0,-1):

        #     for num in buckets[freq]:
        #         result.append(num)

        #         if len(result)==k:
        #             return result


        

        

        