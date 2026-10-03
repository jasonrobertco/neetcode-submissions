class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        A = [0] * 26
        B = [0] * 26
        for i in range(len(s1)):
            A[ord(s1[i]) - ord('a')] += 1
            B[ord(s2[i]) - ord('a')] += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if A == B:
                return True
            B[ord(s2[l]) - ord('a')] -= 1
            B[ord(s2[r]) - ord('a')] += 1
            l += 1
        return A == B