# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0

        def dfs(node):
            nonlocal maxi


            if node is None:
                return 0

        
            left = dfs(node.left)
            right = dfs(node.right)


            diameter = left+right

            maxi = max(maxi,diameter)

            return 1 + max(left,right)


        dfs(root)

        return maxi

    

      