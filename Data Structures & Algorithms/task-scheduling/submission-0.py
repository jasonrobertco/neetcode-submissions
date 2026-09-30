class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 26 slots, one per letter A-Z, all start at 0
        count = [0] * 26

        # count how many times each task appears (A -> index 0, B -> index 1, ...)
        for c in tasks:
            count[ord(c) - ord("A")] += 1

        # maxf = highest frequency (the task that needs the most cooldown gaps)
        maxf = max(count)

        # ties = how many tasks share that highest frequency
        ties = count.count(maxf)

        # (maxf - 1) full rounds of (n + 1) cycles, plus one last slot per tied task
        # max with len(tasks) covers the case where there's no idle time at all
        return max(len(tasks), (maxf - 1) * (n + 1) + ties)