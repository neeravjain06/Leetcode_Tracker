# Last updated: 15/07/2026, 18:00:19
1class Solution(object):
2    def threeSum(self, nums):
3        nums.sort()
4        ans = []
5
6        for i in range(len(nums)):
7
8            # Skip duplicate first numbers
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            left = i + 1
13            right = len(nums) - 1
14
15            while left < right:
16
17                total = nums[i] + nums[left] + nums[right]
18
19                if total < 0:
20                    left += 1
21
22                elif total > 0:
23                    right -= 1
24
25                else:
26                    ans.append([nums[i], nums[left], nums[right]])
27
28                    left += 1
29                    right -= 1
30
31                    # Skip duplicate left values
32                    while left < right and nums[left] == nums[left - 1]:
33                        left += 1
34
35                    # Skip duplicate right values
36                    while left < right and nums[right] == nums[right + 1]:
37                        right -= 1
38
39        return ans