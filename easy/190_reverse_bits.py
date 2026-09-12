class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = bin(n)[2:].zfill(32)
        n = len(binary_n)
        l = 0
        r = n-1
        arr = [0]*n
        while l < r:
            arr[l], arr[r] = str(binary_n[r]), str(binary_n[l])
            l += 1
            r -= 1
        
        return int("".join(arr), 2)
