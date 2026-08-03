class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = 0
        s = str(x)
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True