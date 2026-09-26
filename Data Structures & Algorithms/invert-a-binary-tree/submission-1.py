# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        #while child.next no 0
        #go down depth search
        #left and right at the same time
        #node 1, 2 left 3 right 
        #temp to self.left
        #self.left = self.right
        #self.right = temp
        #go to 2 
        #swap 4 and 5
        #go to 4, nothing
        #go to 5, nothing
        #go to 6, nothing
        #go to 7, nothing

        