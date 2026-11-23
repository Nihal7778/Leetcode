class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        #optimal
        n = len(arr)
        count = 0
        left = 0
        curr_sum = 0


        for right in range(n):
            curr_sum+=arr[right]
            curr_window = right-left+1

            if curr_window>k:
                curr_sum-=arr[left]
                left+=1
                curr_window = right-left+1


            if curr_window == k:
                avg = curr_sum/k

                if avg>=threshold:
                    count+=1

    
        return count


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force
        # n = len(arr)
        # count = 0


        # for i in range(n):
            
        #     curr_sum = 0
        #     for j in range(i,n):
        #         curr_sum+=arr[j]
        #         curr_window = j-i+1


        #         if curr_window == k:
        #             avg = curr_sum/k

        #             if avg>=threshold:
        #                 count+=1

        #             break

        # return count




                    






        