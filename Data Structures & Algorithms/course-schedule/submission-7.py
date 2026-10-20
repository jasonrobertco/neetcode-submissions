class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs attempt
        #mark as visited (add to path)
        #process
        #call dfs on neighbors
        #take course b before a
        #prereqs is inputted as a list


        #build adjacency list
        adj = defaultdict(list)
        for course,prereq in prerequisites:
            adj[course].append(prereq)

        path = set() #make a set
        def dfs(c):
            #process 
            #if its safe it should have no preqreq
            if not adj[c]:
                return True
            #if its already in set or prereq?
            if c in path:
                return False
            #if not in set add the course
            path.add(c)
            #call on prereq
            for p in adj[c]:
                if not dfs(p):
                    return False
            #then clear it
            path.remove(c)
            adj[c] = []
            return True
            #when do i clear the path

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True