class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        for i in range(n-1):
            swapped = False

            for current in range(n-i-1):
                if nums[current]>nums[current+1]:
                    nums[current],nums[current+1]=nums[current+1],nums[current]
                    swapped=True

            if not swapped:
                break

        return nums
        