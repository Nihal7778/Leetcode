class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sums = 0
        dup = x

        while x>0:
            ld = x%10
            sums+=ld
            x = x//10

        if dup%sums == 0:
            return sums

        return -1
        
    

        