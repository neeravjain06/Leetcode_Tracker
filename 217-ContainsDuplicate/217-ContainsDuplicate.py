# Last updated: 08/09/2026, 09:17:27
1class Solution(object):
2    def containsDuplicate(self, nums):
3        seen=set()
4        for i in nums:
5            if i in seen:
6                return True
7            seen.add(i)
8        return False
9        