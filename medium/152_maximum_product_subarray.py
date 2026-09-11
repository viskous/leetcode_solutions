class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = curr_product = 1
        store_negative = None
        for x in range(n):
            if nums[x] == 0:
                if max_product < curr_product: max_product = curr_product
                curr_product = 1

            elif nums[x] < 0:
                if store_negative == None: store_negative = nums[x]
                else:
                    curr_product *= (store_negative*nums[x])
                    store_negative = None
                if max_product < curr_product: max_product = curr_product
            else:
                curr_product *= nums[x]
                if max_product < curr_product: max_product = curr_product
        return max_product
            