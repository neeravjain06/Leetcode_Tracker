# Last updated: 14/07/2026, 23:47:34
1class Solution(object):
2    def isPalindrome(self, s):
3        left=0
4        right=len(s)-1
5
6        while left<right:
7
8            if not s[left].isalnum():
9                left+=1
10            elif not s[right].isalnum():
11                right-=1
12            elif s[left].lower()!=s[right].lower():
13                return False
14            else:
15                left+=1
16                right-=1
17        return True