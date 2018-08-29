#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 1:57
# @Author  : Derek.S
# @Site    : 
# @File    : 37.reverse-3-digit-integer.py

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        listStr=list(str(number))
        i=0
        newList=[]
        newstr=""
        while i<len(listStr):
            f=listStr.pop()
            if f == "0":
                if(len(newList))==0:
                    pass
                else:
                    newList.append(f)
            else:
                newList.append(f)
        return int(''.join(newList))