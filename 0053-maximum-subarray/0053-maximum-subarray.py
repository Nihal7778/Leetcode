class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = float('-inf')
        prefix_sum = 0


        for num in nums:
            
            if prefix_sum<0:
                prefix_sum= num
            
            else:
                prefix_sum+=num


            if prefix_sum>max_subarray:
                max_subarray = prefix_sum

        return max_subarray
        