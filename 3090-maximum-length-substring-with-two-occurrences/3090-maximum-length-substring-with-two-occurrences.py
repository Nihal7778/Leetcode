class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        hashmap = {}

        max_length = 0
        n = len(s)
        for i in range(n):
            hashmap = {}
            for j in range(i,n):
                if s[j] in hashmap:
                    hashmap[s[j]]+=1
                else:
                    hashmap[s[j]]=1

            
                curr_window = j-i+1

                if hashmap[s[j]]>2:
                    break

                max_length = max(max_length,curr_window)

        return max_length






        
        