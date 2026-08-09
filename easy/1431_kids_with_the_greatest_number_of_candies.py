class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = 0
        result = []
        n = len(candies)
        for x in range(n):
            maxx = max(maxx, candies[x])
            result.append(candies[x]+extraCandies)
        for i in range(n):
            if result[i] >= maxx:
                result[i] = True
            else:
                result[i] = False
        return result