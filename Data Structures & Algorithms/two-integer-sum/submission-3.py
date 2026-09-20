class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we want to build this in a way where we store values weve already tried
        #i tink we can do this with a hasmap
        mydict = dict()
        #so now if we seem a number we can add it to the set
        for index, n in enumerate(nums):
            diff = target - n
            if diff in mydict:
                return [mydict[diff], index]
            mydict[n] = index
        return