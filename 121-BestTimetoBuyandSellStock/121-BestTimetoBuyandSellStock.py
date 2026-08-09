# Last updated: 09/08/2026, 23:09:31
1class Solution(object):
2    def maxProfit(self, prices):
3        min=float('inf')
4        max=0
5        for price in prices:
6            if price<min:
7                min=price
8            elif price-min>max:
9                max=price-min
10        return max
11