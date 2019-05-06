#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:38:43 2019

@author: rajeshnarayanarao
"""

thisdict = {
        "Name": "Rajesh",
        "Sex": "Male",
        "Occupation": "Coder"}
name = thisdict["Name"]
sex = thisdict.get("Sex")
thisdict["Age"] = 40

for x in thisdict:
    print(x)
    
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)
    
for x, y in thisdict.items():
    print(x, y)
    
if "Sex" in thisdict:
    print("Yes 'Sex' is one of the keys in the thisdict")
    
print(len(thisdict))

thisdict["origin"] = "Indian"
print(thisdict)
#thisdict.pop("Sex")
#print(thisdict)
#thisdict.popitem()
#print(thisdict)
#del thisdict["Age"]
#print(thisdict)
#del thisdict
#print(thisdict)

#thisdict.clear()
#print(thisdict)


