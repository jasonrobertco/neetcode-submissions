class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            rock1 = heapq.heappop(h)
            rock2 = heapq.heappop(h)
            if rock1 < rock2:
                heapq.heappush(h, rock1-rock2)
        return -h[0] if h else 0
