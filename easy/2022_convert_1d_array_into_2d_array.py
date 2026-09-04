class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        d2_array = []
        k = 0
        curr = 0
        nzxt = n
        print(original[nzxt:nzxt + n])
        if m*n != len(original): return []
        for i in range(m):
            d2_array.append(original[curr:nzxt])
            curr = nzxt
            nzxt += n
        return d2_array