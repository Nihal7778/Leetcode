class Solution:
    def removeDuplicates(self, s: str) -> str:
        #constraints - s is lowercase, 
        # we have to keep removing adj elements in an iteration whose chars are similar and then return non equal elements in a string 
        # cannot rearrange the order

        #algo - i can use a d.s stack for insertion and deletion of elements, if stack is not empty and top of stack matches with character then we can pop the matching element else we can append the char and then conv the stack into a string and return it.

        #Optimal
        n = len(s)
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()

            else:
                stack.append(char)

        return "".join(stack)


        # t.c - O(N)
        # s.c - O(N)


        

                
                



        