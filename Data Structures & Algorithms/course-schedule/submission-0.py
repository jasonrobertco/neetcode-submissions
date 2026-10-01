class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph dict
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        #path set
        path = set()

        def dfs(c):
            #cycke
            if c in path:
                return False
            #no prereqs or taken ignore
            if not graph[c]:
                return True
            #course not taken
            path.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            path.remove(c)
            graph[c] = []
            return True
                
            

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True