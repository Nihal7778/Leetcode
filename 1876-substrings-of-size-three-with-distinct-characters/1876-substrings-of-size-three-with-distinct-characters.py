class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #Optimal
        n = len(s)

        count = 0

        for i in range(n - 3 + 1):
            seen = set()
           
            for j in range(i, i + 3):
                curr_window = j-i+1

                if s[j] not in seen:
                    seen.add(s[j])

                    if len(seen)==3:
                        count+=1

        return count





       
                    


                

                

        