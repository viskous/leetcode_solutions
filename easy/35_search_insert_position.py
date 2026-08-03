class Solution(object):
    def searchInsert(self, nums, target):
        for index, targ in enumerate(nums):
            if targ < target and index != len(nums)-1:
                continue
            elif targ < target and index == len(nums)-1:
                return index + 1
            else:
                return index
        