class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        best = 0
        for n in myset:
            if n-1 not in myset:
                length = 1
                while n+length in myset:
                    length += 1
                best = max (best,length)
        return best