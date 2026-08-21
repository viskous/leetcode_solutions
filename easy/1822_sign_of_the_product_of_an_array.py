class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pr = 1
        for x in nums:
            pr *= x
        if pr > 0: return 1
        elif pr < 0: return -1
        else: return 0
    