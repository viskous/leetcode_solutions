class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        prev = start
        for i in range(1,n):
            prev ^= (start + 2*i)
        
        return prev
