#!/usr/bin/env python3
'''
Author: David Kohler
inkblots.py
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def generate_trace(n, num_w):
    '''
    Generate num_w random walk traces of length n (2D)
    '''
    x_arrays = []
    y_arrays = []

    for i in range(num_w):
        x = np.zeros(n)
        y = np.zeros(n)

        if i > 0:
            #Makes first point of other walks random
            y[0] = np.random.choice(y_arrays[0], 1)
        for i in range(1, n):
            num = np.random.randint(1, 5)
            if num == 1:
                x[i] = x[i-1] + 1
                y[i] = y[i-1]
            elif num == 2:
                x[i] = x[i-1] - 1
                y[i] = y[i-1]
            elif num == 3:
                x[i] = x[i-1]
                y[i] = y[i-1] + 1
            elif num == 4:
                x[i] = x[i-1]
                y[i] = y[i-1] - 1

        minX = np.amin(x)
        factor = (-1*minX)
        for i in range(len(x)):
            x[i] = x[i] + factor

        x_arrays.append(x)
        y_arrays.append(y)

        x2 = list(x)
        for i in range(len(x2)):
            x2[i] = -1*x2[i]

        x_arrays.append(x2)
        y_arrays.append(y)


    return x_arrays, y_arrays


def plot(x_arrays, y_arrays):
    '''
    Plot each array in x_arrays and y_arrays on same plot (2D)
    '''
    for i in range(len(x_arrays)):
        plt.plot(x_arrays[i], y_arrays[i], c='k', lw=3)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
      n = 500000 #Number of steps
      num_w = 3 #Number of walks

      x_arrays, y_arrays = generate_trace(n, num_w)
      plot(x_arrays, y_arrays)
