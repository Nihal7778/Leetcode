class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Optimal
        n = len(s)
        max_len = 0
        left = 0
        seen = set()
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])


            length = right-left+1
            max_len = max(max_len,length)

        return max_len




















        #brute force
        # n = len(s)
        # max_length = 0

        # for i in range(n):
        #     seen = set()

        #     for j in range(i,n):
        #         if s[j] in seen:
        #             break

        #         seen.add(s[j])

        #         length = j-i+1
        #         max_length= max(max_length,length)

        # return max_length





            




        


        


        

       
                

        


       

        

            
        
        

       

        


        