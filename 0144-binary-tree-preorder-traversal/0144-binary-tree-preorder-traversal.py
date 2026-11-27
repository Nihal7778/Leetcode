# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        #iterative dfs
        # stack = [root]
        # result = []
        # if root is None:
        #     return []


        # while stack:
        #     node = stack.pop()

        #     result.append(node.val)
        #     left = node.left
        #     right = node.right

        #     if node.right:
        #         stack.append(right)

        #     if node.left:
        #         stack.append(left)

        # return result


        #recursive dfs
        result = []


        def dfs(node):
            if node is None:
                return 

            result.append(node.val)

            dfs(node.left)

            dfs(node.right)


        dfs(root)
        return result





            


        