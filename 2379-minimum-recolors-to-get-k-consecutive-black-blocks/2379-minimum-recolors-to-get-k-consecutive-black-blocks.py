class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #optimal
        n = len(blocks)
        min_block = float('inf')
        left = 0
        hashmap = {}

        for right in range(n):
            curr_window = right-left+1

            if blocks[right] in hashmap:
                hashmap[blocks[right]]+=1

            else:
                hashmap[blocks[right]]=1

            if curr_window>k:
                hashmap[blocks[left]]-=1
                left+=1
                curr_window = right-left+1

         
            if curr_window == k:       
                if 'B' in hashmap:
                    recolors = k - hashmap['B']
            
                else:
                    recolors = k

            
                min_block = min(min_block,recolors)



        return min_block

               


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # brute force
        # n = len(blocks)
        # min_block = float('inf')

        # for i in range(n-k+1):
        #     hashmap = {}
        #     for j in range(i,i+k):
        #         if blocks[j] in hashmap:
        #             hashmap[blocks[j]]+=1

        #         else:
        #             hashmap[blocks[j]]=1

                    
        #     if 'B' in hashmap:
        #         recolors = k - hashmap['B']
            
        #     else:
        #         recolors = k

            
        #     min_block = min(min_block,recolors)



        # return min_block
                


        