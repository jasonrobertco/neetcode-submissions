# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        #i want to call dfs on each node and ind best path from each node 

        def dfs(Node):
            #recurisve call on neighbors
            #cases
            #no node
            nonlocal best
            if not Node:
                return 0
            right = dfs(Node.right)
            left = dfs(Node.left)
            best = max(best, right + left)
            return 1 + max(left, right)
            #find longest path
        dfs(root)
        return best
