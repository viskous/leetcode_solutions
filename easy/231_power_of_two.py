class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n < 0:
            return False
        a = math.log(n, 2)
        int_n = int(a)
        return a==int_n