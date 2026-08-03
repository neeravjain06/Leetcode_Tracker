# Last updated: 03/08/2026, 09:02:53
1class Solution(object):
2    def isValid(self, s):
3        stack = []
4        pairs = {')': '(', ']': '[', '}': '{'}
5        
6        for ch in s:
7            if ch in "({[":
8                stack.append(ch)
9            else:
10                if not stack or stack[-1] != pairs[ch]:
11                    return False
12                stack.pop()
13        
14        return len(stack) == 0