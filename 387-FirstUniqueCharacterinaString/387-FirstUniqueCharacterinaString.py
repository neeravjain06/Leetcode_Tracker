# Last updated: 03/08/2026, 00:27:48
1class Solution(object):
2    def firstUniqChar(self, s):
3        mp=defaultdict(int)
4        for i in range(len(s)):
5            mp[s[i]]+=1
6        for i in range(len(s)):
7            if mp[s[i]]==1:
8                return i
9        return -1
10
11
12        