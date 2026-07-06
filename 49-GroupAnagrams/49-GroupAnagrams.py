# Last updated: 06/07/2026, 22:19:45
1class Solution(object):
2    def groupAnagrams(self, strs):
3        groups=defaultdict(list)
4
5        for word in strs:
6            key="".join(sorted(word))
7            groups[key].append(word)
8    
9        return list(groups.values())
10
11      
12        