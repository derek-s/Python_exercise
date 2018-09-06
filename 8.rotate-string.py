# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:8.rotate-string.py
# Project:Python_Exercise
# File Created:2018-09-06 11:57:04
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-06 11:57:04
# -----

# 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

# 对于字符串 "abcdefg".

# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"


class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        l = len(str)
        if(l != 0):
            if(offset > l):
                offset = (offset % l)
            for i in range(offset):
                str.insert(0, str.pop())
        return str


if __name__ == "__main__":
    print(Solution().rotateString(list(""), 0))
