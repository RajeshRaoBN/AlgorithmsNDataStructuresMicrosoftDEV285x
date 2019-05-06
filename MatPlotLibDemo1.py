#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:45:32 2019

@author: rajeshnarayanarao
"""

# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
# =============================================================================
import numpy as np
# import pandas
# 
# fig = plt.figure()  # an empty figure with no axes
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is
# 
# fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# 
# a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
# a_asndarray = a.values
# 
# b = np.matrix([[1,2],[3,4]])
# b_asarray = np.asarray(b)
# 
# x = np.linspace(0, 2, 100)
# 
# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
# 
# plt.xlabel('x label')
# plt.ylabel('y label')
# 
# plt.title("Simple Plot")
# 
# plt.legend()
# 
# plt.show()
# 
# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()
# 
# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph
# 
#     Parameters
#     ----------
#     ax : Axes
#         The axes to draw to
# 
#     data1 : array
#        The x data
# 
#     data2 : array
#        The y data
# 
#     param_dict : dict
#        Dictionary of kwargs to pass to ax.plot
# 
#     Returns
#     -------
#     out : list
#         list of artists added
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out
# 
# # which you would then use as:
# 
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(1, 1)
# my_plotter(ax, data1, data2, {'marker': 'D'})
# 
# fig, (ax1, ax2) = plt.subplots(1, 2)
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})
# =============================================================================

import matplotlib
matplotlib.use('PS')   # generate postscript output by default

plt.ion()
plt.plot([1.6, 2.7])

plt.title("interactive test")
plt.xlabel("index")

ax = plt.gca()
ax.plot([3.1,2.2])

plt.draw()

plt.ioff()
plt.plot([1.6, 2.7])

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
