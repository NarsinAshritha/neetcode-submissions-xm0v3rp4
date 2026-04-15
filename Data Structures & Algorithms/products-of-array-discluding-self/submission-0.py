class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Left products
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        # Step 2: Right products
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
        