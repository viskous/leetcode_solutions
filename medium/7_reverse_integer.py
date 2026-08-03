class Solution:
    def reverse(self, x: int) -> int:
        s =str(x) 

        if s[0] == '-':
            rev = '-'+s[:0:-1]
        else:
            rev = s[::-1]
        
        rev = int(rev)

        if rev < -(2**31) or rev > ((2**31)-1):
            return 0
        return rev
        