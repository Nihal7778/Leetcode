# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        #constraints
        #left subtree contains only nodes with keys strictly less than node's key
        #right subtree contains nodes with keys greater than node's key
        #both should be binary search tree

        low = float('-inf')
        high = float('inf')
        def dfs(node,low,high):
            if node is None:
                return True

            if node.val<=low or node.val>=high:
                return False

            left = dfs(node.left,low,node.val)
            right = dfs(node.right,node.val,high)

            return left and right

        
        return dfs(root,low,high)
        