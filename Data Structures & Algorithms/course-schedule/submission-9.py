class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        path = set()

        def dfs(c):
            if not adj[c]:
                return True
            if c in path:
                return False
            #else
            path.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            adj[c] = []
            path.remove(c)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True