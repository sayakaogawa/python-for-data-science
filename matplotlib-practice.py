#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:10:23 2021

Learning basics of matplotlib.
@author: sayaka.ogawa
"""

import numpy as np
import matplotlib.pyplot as plt


def plot1():
    """Note that in one function, even if you assign the plt.plot a variable,
    it will plot all data on one singular plot as opposed to generating a unique
    plot for each variable when using SPyder."""
    # creates a linear-spaced plot from 0-10 with 1000 points
    x = np.linspace(0, 10, 1000)
    
    # set values of y to be sin(x)
    y = np.sin(x)
    
    # plot the points in line form
    # line = plt.plot(x, y)

    # plot in scatter (points) form, sampling all x,y values, but skipping every 10 points
    # scat = plt.scatter(x[::10], y[::10], color='red')    # change color of points using color=

    # plotting more than one group on a single graph
    fig = plt.plot(x,y,color='b')
    fig = plt.plot(x,np.cos(x),color='g')
    
    return fig


def plot2():
    
    x = np.linspace(0, 10, 1000)
    
    # assigning data sets unique lines
    plt.plot(x, x+0, '-g')  # solid green
    plt.plot(x, x+1, '--c') # dashed cyan
    plt.plot(x, x+2, '-.k') # dash-dot black
    plt.plot(x, x+3, ':r')  # dotted red
    


def main():
    
    #fig = plot1()
    plot2()
    
    
    
main()
