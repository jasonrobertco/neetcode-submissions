class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for i, num in enumerate(nums):
            if num in myset:
                return True
            myset.add(num)
        return False
        