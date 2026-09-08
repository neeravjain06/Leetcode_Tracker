# Last updated: 08/09/2026, 09:17:48
class Solution(object):
    def firstUniqChar(self, s):
        mp=defaultdict(int)
        for i in range(len(s)):
            mp[s[i]]+=1
        for i in range(len(s)):
            if mp[s[i]]==1:
                return i
        return -1


        