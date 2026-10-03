class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        A = [0] * 26
        B = [0] * 26

        for i in range(len(s1)):
            A[ord(s1[i]) - ord("a")] += 1
            B[ord(s2[i]) - ord("a")] += 1
        l = 0                            # left edge of the window
        for j in range(len(s1), len(s2)):    # j = new right letter
            if A == B:                   # same counts -> permutation found
                return True
            B[ord(s2[j]) - ord("a")] += 1    # add right letter
            B[ord(s2[l]) - ord("a")] -= 1    # remove left letter
            l += 1

        return A == B 