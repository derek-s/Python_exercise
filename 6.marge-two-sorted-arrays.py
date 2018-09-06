# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:6.marge-two-sorted-arrays.py
# Project:Python_Exercise
# File Created:2018-09-06 11:42:37
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-06 11:42:37
# -----

# 合并两个排序的整数数组A和B变成一个新的数组。
# 给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        return sorted(A + B)


if __name__ == "__main__":
    Solution().mergeSortedArray([1, 2, 3, 4], [2, 4, 5, 6])
