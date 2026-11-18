class Solution:
    def isPalindrome(self, x: int) -> bool:

        dup = x
        count = 0

        while x>0:
            ld = x%10   
            count = (count*10)+ld
            x = x//10
        
        return count == dup
        