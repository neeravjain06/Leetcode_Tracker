# Last updated: 08/09/2026, 09:17:52
class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1
        write = n - 1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] ** 2
                left += 1
            else:
                result[write] = nums[right] ** 2
                right -= 1

            write -= 1

        return result