class Solution:
    def isDecomposable(self, s: str) -> bool:

        count = 1
        result = []

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1

            else:
                result.append(count)
                count = 1

        result.append(count)
        
        count_two = 0

        for count in result:
            if count%3==0:
                continue

            elif count%3==1:
                return False

            else:
                count_two+=1

        return count_two == 1


        