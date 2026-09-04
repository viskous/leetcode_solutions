class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        d2_array = [[0] * n for x in range(m)]
        k = 0
        if m*n != len(original): return []
        for i in range(m):
            for j in range(n):
                d2_array[i][j] = original[k]
                k += 1
        return d2_array