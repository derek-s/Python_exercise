# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# File:1585.moving-stones.py
# Project:Python_Exercise
# File Created:2018-09-01 10:38:11
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2018-09-01 10:38:11
# -----

# 竞赛题目，题目大意：有一方格区域上摆放着棋子，从左至右放，让石子位置等于奇数数列[1, 3, 5, 7, 9 2n-1]或偶数数列[2, 4, 6, 8, 2n]
# 示例输入
# stone = [5, 4, 1] return 1
# 4只需要左移1格等于奇数数列
# stone = [1, 4, 10] return 5

## 看到比赛晚了，没有看完题目就关闭了，于是题目可能不是原题，姑且先做一道。

class Solution:
    def movestones(self, arr):
        # write your cod
        minValue = min(arr)
        maxValue = max(arr)
        lenValue = len(arr)
        nArr = sorted(arr)
        oddSum = 0
        evenSum = 0
        odd = []
        even = []

        if(minValue % 2 == 0):
            for i in range(minValue+1, maxValue, 2):
                odd.append(i)
            for i in range(minValue, maxValue, 2):
                even.append(i)
        else:
            for i in range(minValue, maxValue, 2):
                odd.append(i)
            for i in range(minValue+1, maxValue, 2):
                even.append(i)
        
        for i in (range(0, lenValue)):
            if(odd[i] < nArr[i]):
                oddSum += nArr[i] - odd[i]
            else:
                oddSum += odd[i] - nArr[i]
            
            if(even[i] < nArr[i]):
                evenSum += nArr[i] - even[i]
            else:
                evenSum += even[i] - nArr[i]
            
        if(oddSum > evenSum):
            return evenSum
        else:
            return oddSum


if __name__ == "__main__":
    arr = [1, 4, 10]
    print(Solution().movestones(arr))