#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:27:18 2019

@author: rajeshnarayanarao
"""

#if __name__ == '__main__':
#    x = int(input())
#    y = int(input())
#    z = int(input())
#    n = int(input())
def process(x, y, z, n):
    out = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i + j + k) != n:
                    out.append([i, j, k])
    return(out)
    
process(2, 2, 2, 2)