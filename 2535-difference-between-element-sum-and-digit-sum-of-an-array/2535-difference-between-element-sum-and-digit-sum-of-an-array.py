class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element = sum(nums)
        digit_sum = 0
        

        for num in nums:
            while num>0:
                ld = num%10
                digit_sum+=ld
                num = num//10

        total = element - digit_sum 

        return total





        