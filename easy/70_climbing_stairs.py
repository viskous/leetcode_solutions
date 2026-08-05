class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(0,n+1):
            next = first + second
            first = second
            second = next
        return first