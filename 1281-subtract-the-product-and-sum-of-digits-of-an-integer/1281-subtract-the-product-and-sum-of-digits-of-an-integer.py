class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        prod = 1

        while n>0:
            ld = n%10
            prod*=ld
            sums+=ld

            n = n//10

        total = prod - sums

        return total

        



            

        