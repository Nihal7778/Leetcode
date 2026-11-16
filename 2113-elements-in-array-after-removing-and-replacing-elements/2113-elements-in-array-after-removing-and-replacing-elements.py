class Solution:
    def elementInNums(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        #constraints - since restoration takes n times, removal also takes n times we can cal cyclic_time=time%(2*n)
       
       
        n = len(nums)
        result = []

        for time,index in queries:
            cyclic_time = time%(2*n)

            
            if cyclic_time<=n:
                #removal
                original_index = cyclic_time+index

                if original_index<n:
                    result.append(nums[original_index])

                else:
                    result.append(-1)

            else:
                #restoration
                restored_length = cyclic_time - n

                if index<restored_length:
                    result.append(nums[index])

                else:
                    result.append(-1)

        return result

        
        
