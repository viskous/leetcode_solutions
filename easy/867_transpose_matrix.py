class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        T = [[0] * m for x in range(n)]
        for j in range(n):
            for i in range(m):
                T[j][i] = matrix[i][j]

        return T



        