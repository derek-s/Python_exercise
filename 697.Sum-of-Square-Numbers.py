# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:697.Sum-of-Square-Numbers.py
# Project:Python_Exercise
# File Created:2018-08-31 12:00:14
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-08-31 12:00:14
# -----

# 遍历从0到num的平方根的平方加入集合，计算num-set()内的平方数，若差值在set内，则返回True，遍历结束返回False

class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """
    def checkSumOfSquareNumbers(self, num):
        # write your cod
        if str(num).split("-"):
            if(len(str(num).split("-"))> 1) :
                return False
            else:
                c = int(num ** 0.5)
                d = set()
                f = set()
                
                for i in range(c+1):
                    d.add(i*i)
                for y in d:
                    if((num-y) in d):
                        f.add(y)
                    else:
                        pass
        if(len(f)):
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution().checkSumOfSquareNumbers(18))