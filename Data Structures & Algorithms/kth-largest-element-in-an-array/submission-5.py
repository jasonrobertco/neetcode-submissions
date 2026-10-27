class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            #push to heap want to find the kth LARGEST elements
            #this means that we want the smallest elements at the top to get popped first a minheap does this as the parent is smaller
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        