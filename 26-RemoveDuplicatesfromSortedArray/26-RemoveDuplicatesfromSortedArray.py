# Last updated: 17/07/2026, 22:23:00
1class Solution(object):
2    def removeDuplicates(self, nums):
3        if not nums:
4            return 0
5
6        i = 0
7
8        for j in range(1, len(nums)):
9            if nums[j] != nums[i]:
10                i += 1
11                nums[i] = nums[j]
12
13        return i + 1