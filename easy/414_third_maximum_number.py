class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        s = sorted(s , reverse = True)
        if len(s) < 3:
            return s[0]
        else: return s[2]