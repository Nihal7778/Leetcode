class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        #optimal
        n = len(s)

        hashmap = {}
        max_length = 0
        left = 0

        for right in range(n):


            if s[right] in hashmap:
                hashmap[s[right]]+=1

            else:
                hashmap[s[right]]=1



            while hashmap[s[right]]>2:
                hashmap[s[left]]-=1
                left+=1

            curr_window = right-left+1


            max_length = max(max_length,curr_window)


        return max_length

            

            

       
            





















        #brute force
        # max_length = 0
        # n = len(s)
        # for i in range(n):
        #     hashmap = {}
        #     for j in range(i,n):
        #         if s[j] in hashmap:
        #             hashmap[s[j]]+=1
        #         else:
        #             hashmap[s[j]]=1

            
        #         curr_window = j-i+1

        #         if hashmap[s[j]]>2:
        #             break

        #         max_length = max(max_length,curr_window)

        # return max_length






        
        