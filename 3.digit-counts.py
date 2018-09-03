# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:3.digit-counts.py
# Project:Python_Exercise
# File Created:2018-09-03 11:04:28
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-03 11:04:28
# -----

# 计算数字k在0到n中的出现的次数，k可能是0~9的一个值
# 例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)

class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        lk = []
        tk = []
        for i in range(n+1):
            lk.append(i)
        for x in lk:
            for i in str(x):
                tk.append(i)
        return tk.count(str(k))
        
if __name__ == "__main__":
    Solution().digitCounts(12, 1)