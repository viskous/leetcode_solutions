class Solution:
    def numberOfSteps(self, num: int) -> int:
        num_temp = num
        count = 0
        while True:
            if num_temp == 0:
                return count
            elif num_temp%2== 0:
                num_temp = num_temp//2
                count += 1
            else:
                num_temp -= 1
                count += 1
