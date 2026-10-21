"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #input is always 1
        #undirected?
        #build u
        #make a set to keep track
        copied = {}

        def dfs(node):
            # 1. already copied? return it
            if node in copied:
                return copied[node]
            # 2. make the copy, register it in the dict
            # to make a copy call the class neighbors is empty
            copy = Node(node.val)
            #put old:new
            copied[node] = copy
            # 3. for each neighbor, append dfs(neighbor) to copy.neighbors
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            # 4. return the copy
            return copy


        return dfs(node) if node else None