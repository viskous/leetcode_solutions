class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        n = len(s)
        m = len(t)
        if n == 0 :
            return True
        elif m == 0: return False
        for r in range(m):
            if s[l] == t[r]:
                l += 1
            if l == n:
                return True
        return False
