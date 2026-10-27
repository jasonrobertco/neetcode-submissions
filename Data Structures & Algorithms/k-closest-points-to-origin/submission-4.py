import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return k cloest points to origin
        #parse and create a thruple and sort hashmap or heap
        heap = []
        #closet points = shortest distance = remove "smallest" (largest value)
        for x, y in points:
            heapq.heappush(heap, (-1*(x*x + y*y), x, y)) #pythagorean, dont haveto divide
            while len(heap) > k:
                heapq.heappop(heap)
        res = []
        for n, x, y in heap:
            res.append([x, y])
        return res
            
        