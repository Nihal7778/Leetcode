class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        dup = num


        while num>0:
            ld = num%10
            num = num//10

            if dup%ld == 0:
                count+=1

        return count

        

       



        