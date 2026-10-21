class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        #build adj list
        #course: post reqs
        #build indeg
        #[course] #indegrees
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        #now make a q
        q = deque()
        #if indeg[n] = 0 that is a starter add n to q
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        #make an order empty list
        order = []
        while q:
            #get the n
            n = q.popleft()
            #append to order since we processed it
            order.append(n)
            #look at the adj list process the post reqs
            for x in adj[n]:
                #subtract -1 from the count as we have processed an indegree
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        
        if len(order) == numCourses:
            return order
        return []


            
