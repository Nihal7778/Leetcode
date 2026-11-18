class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Optimal
        nums.sort()

        n = len(nums)
        seen = set(nums)

        result = []

        for i in range(n):
            left = i+1
            right = n-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]

                if total == 0:
                    triplet = (nums[i],nums[left],nums[right])

                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))

                    left+=1
                    right-=1

                elif total<0:
                    left+=1

                else:
                    right-=1

        return result


        T.C- O(n**2), S.C - 0(1)




        # Brute force
        # result = []

        # n = len(nums)

        # seen = set(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = tuple(sorted([nums[i],nums[j],nums[k]]))

        #                 if triplet not in seen:
        #                     seen.add(triplet)
        #                     result.append(list(triplet))
        
        # return result




        
                        


        

     

        