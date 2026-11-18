class Solution:
    def alternateDigitSum(self, n: int) -> int:
        #left to right
        sign = 1
        total = 0

        for char in str(n):
            ld = int(char)
            total+=ld*sign
            sign*=-1

        return total



        # right to left
        # total = 0
        # sign = 1
        # digit_count = 0

        # while n>0:
        #     ld = n%10
        #     total+=sign*ld
        #     sign*=-1
        #     digit_count+=1
        #     n = n//10

        # if digit_count%2 == 0:
        #     return -total

        # return total

        






        