class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        n = len(nums)

        nums.sort()
        for i in range(n-1):
            if nums[i]+1 != nums[i+1]:
                return False

        return True

        
            


        