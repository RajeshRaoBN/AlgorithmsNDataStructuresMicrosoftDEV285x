#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:39:40 2019

@author: rajeshnarayanarao
"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    output = 0
    for i in range(0, n):
        output += (n - i) * 10 ** i
    print(output)