class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = 0
        maxx = 0
        count = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            if maxx < count:
                maxx = count
                index = i
            count = 0
        return [index, maxx]
            