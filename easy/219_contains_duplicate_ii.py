class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        r = 0
        dictt = {}
        while r != n:
            X = dictt.get(nums[r])
            if X != None:
                if abs(X - r) <= k:
                    return True
                else:
                    dictt[nums[r]] = r
            else:
                dictt[nums[r]] = r
            r += 1
        return False










