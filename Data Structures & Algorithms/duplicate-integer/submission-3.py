class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #i forgot syntax
        #base case list does not contain a duplicate element return false
        #case list does contain a duplicate element return true
        #if List is empty then return false (no dup el)
        #create a set
        #for each elemnt in the list check if it is in the set
        #if in the set then return true
        #if it is not in the set then add it to the set
        #attempt
        myset = set()
        for num in nums:
            if num in myset:
                return True
            else:
                myset.add(num)
        return False

