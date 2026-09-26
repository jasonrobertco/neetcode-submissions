class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in mydict:
                return[mydict[diff], index]
            else:
                mydict[value] = index