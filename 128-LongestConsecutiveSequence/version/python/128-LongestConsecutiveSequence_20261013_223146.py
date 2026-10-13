# Last updated: 13/10/2026, 22:31:46
1
2class Solution(object):
3    def longestConsecutive(self, nums):
4        seen = set(nums)
5        longest_streak = 0
6
7        for i in seen:
8            if i - 1 not in seen:
9                current = i
10                length = 1
11
12                while current + 1 in seen:
13                    current += 1
14                    length += 1
15
16                longest_streak = max(longest_streak, length)
17
18        return longest_streak
19