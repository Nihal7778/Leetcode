class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
            
        max_product = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]
        
        
        for i in range(1,len(nums)):
            num = nums[i]
            if num < 0:
                curr_max,curr_min = curr_min,curr_max
                
            if curr_max*num>num:
                curr_max *=num
            else:
                curr_max = num

            if curr_min*num<num:
                curr_min*=num
            else:
                curr_min = num

            if curr_max>max_product:
                max_product = curr_max

        return max_product






                    


        