class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #constraints - the element in nums2 should have greater element located on right side, if we dont find any elements then return -1
        #all elements of nums1 is in nums2, and there are no duplicates as well so no need of sets
        

        #algo- I'll use a monotonic decreasing stack to track elements that haven't found their next greater element. Whenever I encounter a larger element, I'll pop all smaller elements and map them to the current element. Finally, I'll traverse nums1 and retrieve the next greater value from the hashmap, returning -1 when none exists.


        stack = []

        hashmap = {}

        result = []



        for current in nums2:
            while stack and current >stack[-1]:
                popped = stack.pop()
                hashmap[popped] = current

            stack.append(current)


        for num in nums1:
            if num in hashmap:
                result.append(hashmap[num])

            else:
                result.append(-1)


        return result




        

        