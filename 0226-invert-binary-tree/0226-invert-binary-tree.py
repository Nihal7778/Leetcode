# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        #dfs
        # if root is None:
        #     return None

        # root.left,root.right = root.right,root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root    


        #bfs
        if root is None:
            return None

        q = deque([root])

        while q:
            size = len(q)

            

            for _ in range(size):
                node = q.popleft()
                node.left, node.right = node.right, node.left
            

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)


        return root
        



# 1. Check if the node is None (base case).
# 2. Swap its left and right children.
# 3. Recursively visit the left subtree.
# 4. Recursively visit the right subtree.