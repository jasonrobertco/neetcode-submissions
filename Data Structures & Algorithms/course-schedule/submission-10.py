class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)

        path = set()
        
        def dfs(n):
            if not adj[n]:
                return True
            if n in path:
                return False
            path.add(n)
            for p in adj[n]:
                if not dfs(p):
                    return False
            adj[n] = []
            path.remove(n)
            return True
            

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
            
        