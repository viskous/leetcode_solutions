class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        count = 0
        extra = abs(len(a) - len(b))
        if x > y:
            b = "0"*extra + b
        else:
            a = "0"*extra + a
        for i in range(len(a)):
            if a[i] != b[i]: count += 1
        return count

