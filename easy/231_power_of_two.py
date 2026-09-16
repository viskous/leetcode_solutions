class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while True:
            power_2 = 2**i
            if power_2 == n: return True
            if power_2 > n: return False
            i += 1