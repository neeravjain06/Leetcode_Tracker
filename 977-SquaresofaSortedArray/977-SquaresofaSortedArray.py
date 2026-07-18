# Last updated: 18/07/2026, 16:39:19
1class Solution(object):
2    def sortedSquares(self, nums):
3
4        n = len(nums)
5
6        result = [0] * n
7
8        left = 0
9        right = n - 1
10        write = n - 1
11
12        while left <= right:
13
14            if abs(nums[left]) > abs(nums[right]):
15                result[write] = nums[left] ** 2
16                left += 1
17            else:
18                result[write] = nums[right] ** 2
19                right -= 1
20
21            write -= 1
22
23        return result