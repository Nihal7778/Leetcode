class Solution:
    def maximumSumScore(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        max_score = float('-inf')

        prefix_sum = 0

        for num in nums:
            prefix_sum+=num

            suffix_sum = total_sum - prefix_sum + num

            score = max(prefix_sum,suffix_sum)

            max_score = max(max_score,score)

        return max_score




            



        