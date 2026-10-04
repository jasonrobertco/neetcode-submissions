class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            heapq.heappush(h, (-1*(x*x + y*y), x, y))#tuple
            while len(h) > k:
                heapq.heappop(h)
        res = []
        for t, x, y in h:
            res.append([x, y])
        return res
