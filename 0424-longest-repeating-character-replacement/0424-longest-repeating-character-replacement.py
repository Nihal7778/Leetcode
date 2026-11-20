class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Optimal
        n = len(s)
        max_len =0
        left = 0 
        hashmap = {}
        max_freq = 0

        for right in range(n):
            if s[right] in hashmap:
                hashmap[s[right]]+=1

            else:
                hashmap[s[right]]=1

            max_freq = max(max_freq,hashmap[s[right]])

            curr_length = right - left+1

            if curr_length - max_freq > k:
                hashmap[s[left]]-=1
                left+=1
            

            if curr_length - max_freq<=k:
                max_len = max(max_len,curr_length)

        return max_len


           

        

     
















        #brute force
        # n = len(s)
        # max_len = 0
       

        # for i in range(n):
        #     hashmap = {}
        #     max_freq = 0

        #     for j in range(i,n):
        #         if s[j] in hashmap:
        #             hashmap[s[j]]+=1
                
        #         else:
        #             hashmap[s[j]]=1

        #         max_freq = max(max_freq,hashmap[s[j]])

        #         curr_length = j-i+1

        #         if curr_length - max_freq<=k:
        #             max_len = max(max_len,curr_length)

        # return max_len






        