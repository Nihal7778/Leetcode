class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i,val in enumerate(nums):
            k = target - val
            if k in seen:
                return[seen[k],i]

            seen[val] = i
        