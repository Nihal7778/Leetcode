class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(1,num+1):
            digit_sum = 0
            n = i

            while n>0:
                ld = n%10
                digit_sum +=ld
                n = n//10

            if digit_sum%2 == 0:
                count+=1

        return count



        



            


        