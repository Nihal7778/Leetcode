class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        #optimal
        n = len(operations)
        stack = []
        score = 0


        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])

            elif op == 'D':
                stack.append(2*stack[-1])

            elif op == 'C':
                stack.pop()

            else:
                stack.append(int(op))

        
        return sum(stack)
            


        #algo
        # I'll use a stack because every operation depends on the most recent valid scores. I'll traverse the operations once, push new scores and pop cancelled scores. Finally, I'll sum the remaining scores. This gives O(n) time and O(n) space.

        


