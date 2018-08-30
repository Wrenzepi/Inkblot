#!/usr/bin/env python3
'''
Author: David Kohler
inkblots.py
'''

import numpy as np
import plotly
import plotly.graph_objs as go


def generate_trace(n, data=[]):
    '''
    Generate a random walk trace of length n (2D)
    '''

    x = np.zeros(n)
    y = np.zeros(n)

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

    trace = go.Scatter(
        x = x,
        y = y,
        marker=dict(
            color='black'
        ),
        line=dict(
            width=6
        )
    )

    data.append(trace)

    x2 = x[:]
    for i in range(len(x2)):
        x2[i] = -1*x2[i]

    trace = go.Scatter(
        x = x2,
        y = y,
        marker=dict(
            color='black'
        ),
        line=dict(
            width=6
        )
    )

    data.append(trace)


    return data


def plot(data):
    '''
    Plot each array in data on same plot
    '''
    layout = go.Layout(
        title='Inkblot',
        margin=dict(
            l=0,
            r=0,
            b=25,
            t=50
        ),
        xaxis=dict(
            title='',
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False
        ),
        yaxis=dict(
            title='',
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False
        )
    )

    fig = go.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename='Inkblot.html')


if __name__ == '__main__':
      n = 100000
      data1 = generate_trace(n)
      data2 = generate_trace(n, data1)
      data3 = generate_trace(n, data2)
      plot(data3)
