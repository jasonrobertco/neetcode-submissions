class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub = t 
        full = s
        subcounts = {}
        for c in sub:
            subcounts[c] = subcounts.get(c, 0) + 1
        fullcounts = {}
        need = len(subcounts)
        matches = 0
        best_len = len(full) + 1
        best_start = 0
        L = 0
        for R in range(len(full)):
            c = full[R]
            fullcounts[c] = fullcounts.get(c, 0) + 1
            if c in subcounts and fullcounts[c] == subcounts[c]:
                matches += 1

            # shrink while the window is valid
            while matches == need:
                if R - L + 1 < best_len:
                    best_len = R - L + 1
                    best_start = L
                c = full[L]
                fullcounts[c] -= 1
                if c in subcounts:
                    if fullcounts[c] < subcounts[c]:
                        matches -= 1
                L += 1

        if best_len == len(full) + 1:
            return ""

        answer = ""
        for i in range(best_start, best_start + best_len):
            answer += full[i]
        return answer
            

