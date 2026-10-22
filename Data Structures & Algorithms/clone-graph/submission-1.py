"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {} #

        def dfs(node):
            #val
            #alraeady bene processed
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val)

            #add to hashmap
            #key:value oldnode:copy
            oldtonew[node] = copy
            #neighbors
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        return dfs(node) if node else None

        