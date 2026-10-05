class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph 
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        #currentset
        currentset = set()
        #dfs
        def dfs(node):
            #alr in the current set
            if node in currentset:
                return False
            #node [] empty
                #ale current true
            if not graph[node]:
                return True
            #node current.add
            currentset.add(node)
            #look at neighbors
            for prereq in graph[node]:
                #call dfs on edges
                if not dfs(prereq):
                    return False
            #remove vertex current path
            currentset.remove(node)
            #set edges to []
            graph[node] = []
            #return true dfs succesful
            return True
                   
        #call dfs on eveyr course
            #any false return false
        #return true
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
                
        