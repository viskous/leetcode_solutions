class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        r = n -1 
        l = 0
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

