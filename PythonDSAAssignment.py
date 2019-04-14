#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:45:10 2019

@author: rajeshnarayanarao
"""

# Assignment: Write a program that counts from 1 to 10



# increment = 1
#class test:
#    def count(start, end, increment):
#        total = 0
#        for elements in range(start, end, increment):
#            total += elements
#        return total
#    
#    print(count(1, 10, 1))
#
#aName = input("Please enter your name ")
#print("Your name in all capitals is",aName.upper(),
#      "and has length", len(aName))

#wordlist = ['cat','dog','rabbit']
#letterlist = []
#for animal in wordlist:
#    for letter in animal:
#        letterlist.append(letter)
#print(list(set(letterlist)))

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        
        self.num = top
        self.den = bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
#        newnum = self.num*otherfraction.den + self.den*otherfraction.num
#        newden = self.den * otherfraction.den
#
#        return Fraction(newnum,newden)

myfraction = Fraction(3, 5)
print(myfraction)
print("I ate ", myfraction, " of my Pizza")
myfraction.__str__()
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 =f1+f2
print(f3)