class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        original = num
        reversed1 = 0 

        while num>0:
            ld = num%10
            reversed1 = (reversed1*10)+ld
            num = num//10
            
        reversed2 = 0
        while reversed1>0:
            ld = reversed1%10
            reversed2 = (reversed2*10)+ld
            reversed1 = reversed1//10


        return reversed2 == original

        







        