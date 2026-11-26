# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        #dfs
        # if root is None:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return 1 + max(left,right)

   



        #bfs
        if root is None:
            return 0

        q = deque([root])
        depth =0 

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                left = node.left
                right = node.right

                if left:
                    q.append(left)


                if right:
                    q.append(right)

            depth+=1

        return depth

        