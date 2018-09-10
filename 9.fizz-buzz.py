# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:9.fizz-buzz.py
# Project:Python_Exercise
# File Created:2018-09-10 01:13:30
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-10 01:13:30
# -----

# 给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

# 如果这个数被3整除，打印fizz.
# 如果这个数被5整除，打印buzz.
# 如果这个数能同时被3和5整除，打印fizz buzz.

# 比如 n = 15, 返回一个字符串数组：

# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz", "11", "fizz",
#   "13", "14", "fizz buzz"
# ]


class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        ret = [str(i) for i in range(1, n+1)]

        i = 0
        while i < n - 2:
            ret[i + 2] = "fizz"
            i = i + 3

        i = 0
        while i < n - 4:
            if ret[i + 4] == "fizz":
                ret[i + 4] = "fizz buzz"
            else:
                ret[i + 4] = "buzz"
            i = i + 5
        return ret

if __name__ == "__main__":
    print(Solution().fizzBuzz(15))