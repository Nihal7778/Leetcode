class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:



        #algo - first take a ds min heap since i have to find lowest element and multiply it with multiplier then next
        #iterate all elements of input and heapify minheap and before that since we have to preserve the order i could return final state by storing original index along with its value. write another loop where we store heapq.heappop in value and index and then at each operation we multiply the lowest number in array with multiplier and then replace nums[index] = value and push 


        minheap = []

        
        for index,value in enumerate(nums):
            heapq.heappush(minheap,(value,index))


        for i in range(k):
            value,index = heapq.heappop(minheap)

            value = value*multiplier

            nums[index] = value

            heapq.heappush(minheap,(value,index))

        return nums





        