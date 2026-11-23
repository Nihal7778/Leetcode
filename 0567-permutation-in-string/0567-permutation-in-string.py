class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #optimal
        m = len(s1)
        n = len(s2)
        hashmap1 = {}
        hashmap2 = {}
        left = 0


        if len(s2)<len(s1):
            return False

        for i in range(m):
            if s1[i] in hashmap1:
                hashmap1[s1[i]]+=1

            else:
                hashmap1[s1[i]]=1

            if s2[i] in hashmap2:
                hashmap2[s2[i]]+=1

            else:
                hashmap2[s2[i]]=1

        if hashmap1 == hashmap2:
            return True

          
        for right in range(m,n):

            if s2[right] in hashmap2:
                hashmap2[s2[right]]+=1

            else:
                hashmap2[s2[right]]=1

            hashmap2[s2[left]]-=1

            if hashmap2[s2[left]] == 0:
                del hashmap2[s2[left]]


            left+=1

    
            if hashmap1== hashmap2:
                return True

        return False


































        #brute force
        # m = len(s1)
        # n = len(s2)
        # hashmap1 = {}

        # if len(s2)<len(s1):
        #     return False


        # for i in range(m):
        #     if s1[i] in hashmap1:
        #         hashmap1[s1[i]]+=1

        #     else:
        #         hashmap1[s1[i]]=1

          
        # for i in range(n-m+1):
        #     hashmap2 = {}

        #     for j in range(i,n):
        #         if s2[j] in hashmap2:
        #             hashmap2[s2[j]]+=1

        #         else:
        #             hashmap2[s2[j]]=1

                
        #         curr_window = j-i+1

        #         if curr_window == m:
        #             if hashmap1== hashmap2:
        #                 return True

        #             break

        # return False

        
 