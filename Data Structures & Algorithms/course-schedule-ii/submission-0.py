class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        path = set()
        visited = set()
        output = []

        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            path.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            path.remove(c)
            visited.add(c)
            output.append(c)     # all of c's prereqs are already in output
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output