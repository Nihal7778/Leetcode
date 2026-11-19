class Solution:
    def maxArea(self, height: list[int]) -> int:
        #Optimal
        max_area = 0
        left= 0
        right = len(height)-1


        while left<right:
            dist = right - left


            if height[right]<height[left]:
                eff_height = height[right]
                
            else:
                eff_height = height[left]

            if height[left] < height[right]:
                left += 1
                
            else:
                right -= 1

                
            curr_area = dist*eff_height

            if curr_area>max_area:
                max_area = curr_area

        return max_area
     


        #Brute force
        # n = len(height)
        # max_area = 0


        # for i in range(n):
        #     for j in range(i+1,n):
        #         dist = j - i

        #         if height[j]<height[i]:
        #             eff_height = height[j]
                
        #         else:
        #             eff_height = height[i]

                
        #         curr_area = dist*eff_height

        #         if curr_area>max_area:
        #             max_area = curr_area

        # return max_area


                
        