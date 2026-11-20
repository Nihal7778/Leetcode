class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)

        left = 0
        curr_sum = 0
        avg = 0
        max_avg = float('-inf')

        for right in range(len(nums)):
            curr_length = right-left+1

            curr_sum+=nums[right]

            if curr_length>k:
                curr_sum-=nums[left]
                left+=1
                curr_length = right - left + 1


            if curr_length == k:
                avg = curr_sum/k

                max_avg = max(max_avg,avg)

        return max_avg

            

            
        
























        # max_avg = float('-inf')
        # n = len(nums)


        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i,n):
        #         curr_sum +=nums[j]
        #         curr_length = j-i+1
                
        #         if curr_length == k:
        #             avg = curr_sum/k
        #             if avg>max_avg:
        #                 max_avg=avg
        #             break
                

        # return max_avg

