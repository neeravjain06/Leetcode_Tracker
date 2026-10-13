# Last updated: 13/10/2026, 22:36:24
class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result