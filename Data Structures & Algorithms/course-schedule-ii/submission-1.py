class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
	#kahns
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for course, prereq in prerequisites:
            adj[prereq].append(course) #add post coureses
            indeg[course] += 1 #add indeg to that post course
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for n in adj[x]:
                indeg[n] -= 1
                if indeg[n] == 0:
                    q.append(n)
        if len(order) == numCourses:
            return order
        return []
        