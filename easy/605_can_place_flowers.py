class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = len(flowerbed)
        count_zero = count_flower = 0
        if i > 1:
            if (flowerbed[0] == 0 and flowerbed[1] == 0): 
                flowerbed[0] = 1
                count_flower += 1
            if (flowerbed[-1] == 0 and flowerbed[-2] == 0):
                flowerbed[-1] = 1
                count_flower += 1
        elif i == 1 and flowerbed[0] == 0:
            count_flower += 1
        for r in range(i):
            if flowerbed[r] == 1:
                if count_zero > 0 and count_zero%2 == 0:
                    count_flower += (count_zero//2 - 1)
                elif count_zero > 0:
                    count_flower += count_zero//2
                count_zero = 0
            else:
                count_zero += 1
        return (n <= count_flower)

            
        