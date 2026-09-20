class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 #2vars to assign pointers
        while l < r: #haven't crossed each other
        #while loops just for skipping skip over characters
            while l < r and not s[l].isalnum(): 
                l += 1 #move forward
            while l < r and not s[r].isalnum():
                r -= 1 #move backward
            if s[l].lower() != s[r].lower(): #ignores case
                return False
            l += 1 #actually moves forward
            r -= 1
        return True


