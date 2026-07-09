# Last updated: 09/07/2026, 21:53:51
1from collections import defaultdict
2
3class Solution(object):
4    def isValidSudoku(self, board):
5        rows = defaultdict(set)
6        cols = defaultdict(set)
7        boxes = defaultdict(set)
8
9        for row in range(9):
10            for col in range(9):
11
12                value = board[row][col]
13
14                if value == ".":
15                    continue
16
17                box = (row // 3, col // 3)
18
19                if (
20                    value in rows[row] or
21                    value in cols[col] or
22                    value in boxes[box]
23                ):
24                    return False
25
26                rows[row].add(value)
27                cols[col].add(value)
28                boxes[box].add(value)
29
30        return True