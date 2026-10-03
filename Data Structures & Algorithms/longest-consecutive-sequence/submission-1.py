class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        best = 0
        for num in myset:
            if num-1 not in myset: #start of seq
                length = 1
                while num+length in myset:
                    length = length+1
                best = max(best,length)
        return best