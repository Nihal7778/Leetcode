class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m>n:
            return False

        hashmap1 = {}
        hashmap2 = {}

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
            left = right-m

            hashmap2[s2[left]]-=1

            if hashmap2[s2[left]]==0:
                del hashmap2[s2[left]]

            if s2[right] in hashmap2:
                hashmap2[s2[right]]+=1

            else:
                hashmap2[s2[right]]=1

            if hashmap1 == hashmap2:
                return True

        return False
        