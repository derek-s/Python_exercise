# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:2.trailing-zeros.py
# Project:Python_Exercise
# File Created:2018-08-31 05:18:44
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-08-31 05:18:44
# -----

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        while n>0:
            count += n//5
            n //= 5
        return count

if __name__ == "__main__":
    print(Solution().trailingZeros(23))