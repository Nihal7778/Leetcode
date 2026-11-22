class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #optimal
        
        n=len(nums)
        seen = set()
        left = 0

        for right in range(n):
            if right - left>k:
                seen.remove(nums[left])
                left+=1

            if nums[right] in seen:
                return True

            seen.add(nums[right])

        return False


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #brute force
        # n=len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True 
        # return False

                


                

            



        