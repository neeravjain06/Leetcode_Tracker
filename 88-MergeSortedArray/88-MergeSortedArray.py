# Last updated: 19/07/2026, 21:59:21
1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        p1=m-1
4        p2=n-1
5        write=m+n-1
6
7        while p1!=-1 and p2!=-1:
8            if nums1[p1]<=nums2[p2]:
9                nums1[write]=nums2[p2]
10                p2-=1
11                write-=1
12                
13            else:
14                nums1[write]=nums1[p1]
15                p1-=1
16                write-=1
17        while p2 >= 0:
18            nums1[write] = nums2[p2]
19            p2 -= 1
20            write -= 1
21