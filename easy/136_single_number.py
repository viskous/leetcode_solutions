class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pr = 0
        for x in nums: pr ^= x
        return pr