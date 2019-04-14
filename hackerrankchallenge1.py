#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:24:51 2019

@author: rajeshnarayanarao
"""

def weirdOrNot(n):
    if n%2 == 1:
        print("Weird")
    elif n >= 2 and n <=5:
        print("Not Weird")
    elif n >= 6 and n <=20:
        print("Weird")
    elif n > 20:
        print("Not Weird")