class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        order = []
        q = deque()
        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        while q:
            c = q.popleft() #current course
            order.append(c) #add to order
            for post in adj[c]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
        if len(order) == numCourses:
            return order
        return []