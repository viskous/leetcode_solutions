class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        while zero > 0:
            nums[l] = 0
            l += 1
            zero -= 1
        while one > 0:
                nums[l] = 1
                l += 1
                one -= 1
        while two > 0:
                nums[l] = 2
                l += 1
                two -= 1
            
            

        