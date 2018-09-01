# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:1.a-b-problem.py
# Project:Python_Exercise
# File Created:2018-08-31 05:49:51
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-08-31 05:49:51
# -----

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        if(self.check(a)):
            if(self.check(b)):
                return self.add(a, b)
            else:
                return self.add(a, self.add((~b), 1))
    
    def add(self, a, b):
        t = a^b
        b = (a&b)<<1;
        if(b != 0):
            return self.add(t, b)
        else:
            return t


if __name__ == "__main__":
    print(Solution().aplusb(1, 2))