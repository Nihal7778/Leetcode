class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        min_num = nums[0]

        for num in nums:
            if num<min_num:
                min_num = num

        total = 0

        while min_num>0:
            digit = min_num%10
            total+=digit
            min_num//=10

        return 0 if total%2!=0 else 1

        