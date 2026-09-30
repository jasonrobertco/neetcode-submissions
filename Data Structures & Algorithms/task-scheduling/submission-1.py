class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # dict of task -> frequency
        count = Counter(tasks)

        # negate counts so heapq (a min-heap) acts like a max-heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)   # turns the list into a heap in O(k)

        time = 0                 # current CPU cycle
        q = deque()              # cooldown queue: [remaining (negative) count, time it's ready again]

        # keep going while tasks are ready OR waiting on cooldown
        while maxHeap or q:
            time += 1            # each loop iteration is one cycle

            if maxHeap:
                # pop the most frequent task; +1 moves the negative count toward 0
                # (running it once means one fewer left)
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:          # cnt != 0 means runs remain
                    # it can run again after n cycles of cooldown
                    q.append([cnt, time + n])

            # if the oldest task in the queue finished cooling down, put it back in the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time