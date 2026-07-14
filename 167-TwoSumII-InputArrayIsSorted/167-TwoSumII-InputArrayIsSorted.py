# Last updated: 14/07/2026, 23:56:11
1class Solution(object):
2    def twoSum(self, numbers, target):
3        left = 0
4        right = len(numbers) - 1
5
6        while left < right:
7
8            curr = numbers[left] + numbers[right]
9
10            if curr < target:
11                left += 1
12
13            elif curr > target:
14                right -= 1
15
16            else:
17                return [left + 1, right + 1]