class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            heapq.heappush(h, (-(x*x + y*y), x, y))
            if len(h) > k:
                heapq.heappop(h)
        #dotn need to heapq.heapify(h)
        #then heap
        #turn back into points
        #(-dist, x, y)
        return [[x,y] for _, x, y in h]