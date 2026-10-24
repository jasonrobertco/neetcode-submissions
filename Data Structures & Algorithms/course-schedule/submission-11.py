class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #trying kahns
            #adj list
            #indegrees
            #order
            #0 preqreqs
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        for course, pre in prerequisites:
            adj[pre].append(course) #append all preqs to build adj list
            indegrees[course] += 1 #add 1 to num indegrees
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        takenorder = []
        while q:
            course = q.popleft() #current course with 0 indegrees
            #add to taken order
            takenorder.append(course)
            #look for next successor, adj[pre] is a list of all the post courses
            for post in adj[course]:
                indegrees[post] -= 1
                if indegrees[post] == 0:
                    q.append(post)
        return len(takenorder) == numCourses