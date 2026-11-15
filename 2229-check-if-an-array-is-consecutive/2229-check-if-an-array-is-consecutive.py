class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        n = len(nums)

        min_num = nums[0]
        max_num = nums[0]
        

        for curr_num in nums:
            if curr_num<min_num:
                min_num = curr_num

            elif curr_num > max_num:
                max_num = curr_num

        if max_num-min_num+1!= len(nums):
            return False

        i = 0

        while i < len(nums):
            corr_index = nums[i]-min_num

            if corr_index==i:
                i+=1

            elif nums[i]==nums[corr_index]:
                return False
            
            else:
                nums[i],nums[corr_index]=nums[corr_index],nums[i]

        return True








        
            


        