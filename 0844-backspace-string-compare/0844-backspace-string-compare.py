class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #constraints
        
        #brute force
        stack1 = []
        stack2 = []

        for char in s:
            if char == '#':
                if stack1:
                    stack1.pop()

            else:
                stack1.append(char)
                
            

        for chars in t:
            if chars == '#':
                if stack2:
                    stack2.pop()

            else:
                stack2.append(chars)


        return stack1 == stack2

       
        