class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            digit_count = 0
            while num>0:
                digit_count+=1

                num = num//10

            if digit_count%2 == 0:
                count+=1

        return count
        