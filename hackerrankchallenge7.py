#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:05:40 2019

@author: rajeshnarayanarao
"""

def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

nums = list(range(1,11))
obj = naive_grouper(nums, 2)

for _ in naive_grouper(range(100000000), 10):
    pass