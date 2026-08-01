class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(0,len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map:
                return [hash_map[compliment], i]
            else:
                hash_map[nums[i]] = i