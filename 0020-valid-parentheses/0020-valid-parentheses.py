class Solution:
    def isValid(self, s: str) -> bool:
        #constraints
        # Open brackets must be closed by the same type of brackets.
        # Open brackets must be closed in the correct order.
        # Every close bracket has a corresponding open bracket of the same type.
        # s consists of parentheses only '()[]{}'


        #algo - my idea is first i will store matching pairs inside a dict and then iterate through the input, if i come across any opening brackets during this process i would append all char else return false and then check if top of stack if it doesnt match the char inside the pair then return false else pop the elements and in the end if stack is empty that means all elements have been succesfully processed and removed.

        #Optimal

        stack = []

        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack)==0





                


        