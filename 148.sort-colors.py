# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:148.sort-colors.py
# Project:Python_Exercise
# File Created:2018-09-04 11:18:57
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-04 11:18:57
# -----

# 给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。
# 我们可以使用整数 0，1 和 2 分别代表红，白，蓝。
# 不能使用代码库中的排序函数来解决这个问题。
# 排序需要在原数组中进行。

# 样例 给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        z = 0
        o = 0
        t = 0
        for x in nums:
            if(x == 0):
                z += 1
            elif(x == 1):
                o += 1
            elif(x == 2):
                t += 1
        for y in range(len(nums)):
            if(z != 0):
                nums[y] = 0
                z -= 1
            elif(z == 0 and o != 0):
                nums[y] = 1
                o -= 1
            elif(z == 0 and o == 0 and t != 0):
                nums[y] = 2
                t -= 1


if __name__ == "__main__":
    nums = [2, 0, 0, 1, 2, 0, 2]
    Solution().sortColors(nums)
