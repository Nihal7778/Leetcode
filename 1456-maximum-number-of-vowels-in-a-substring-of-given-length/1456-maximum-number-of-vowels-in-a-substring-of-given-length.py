class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #optimal
        n = len(s)

        left = 0
        count = 0
        max_vowel = 0

        for right in range(n):
            curr_window = right-left+1



            if s[right] in "aeiou":
                count+=1

            if curr_window>k:
                if s[left] in "aeiou":
                    count-=1
                    
                left+=1
                curr_window = right-left+1
                

            if curr_window == k:
                max_vowel = max(max_vowel,count)

            
        
        return max_vowel



            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force
        # n = len(s)
        # max_vowel = 0



        # for i in range(n-k+1):
        #     count = 0
        #     for j in range(i,n):

        #         curr_window = j-i+1

        #         if s[j] in "aeiou":
        #             count+=1

        #         if curr_window == k:
        #             max_vowel = max(max_vowel,count)
        #             break

        # return max_vowel


                




                
        