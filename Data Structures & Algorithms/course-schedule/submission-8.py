class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make a adj list
        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)
        path = set()

        def dfs(c):
            if not adj[c]: #empty
                return True
            if c in path:
                return False
            #seen is not in path
            path.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            adj[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            

        