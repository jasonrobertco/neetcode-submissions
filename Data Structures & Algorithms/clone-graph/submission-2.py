"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(n):
            if n in seen:
                return seen[n]
            #call constructor
            copy = Node(n.val) #copy is now init with a value
            #add copy to hashmap
            seen[n] = copy
            for nei in n.neighbors: # go ahead and traverse its neighbords
                copy.neighbors.append(dfs(nei)) #for .neighbors call dfs
            return copy
            


        return dfs(node) if node else None
            
        
        