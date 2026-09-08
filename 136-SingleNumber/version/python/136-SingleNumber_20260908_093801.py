# Last updated: 08/09/2026, 09:38:01
1class Solution:
2    def singleNumber(self, nums):
3        result = 0
4
5        for num in nums:
6            result ^= num
7
8        return result