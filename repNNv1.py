#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:15:55 2022

@author: srilthe
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random

layers = []
nodes = []
XY = []
NN = np.array([4,6,6,5])
MAX = max(NN)
WIDTH = MAX/len(NN)
DIF = (MAX - NN)/2
XY = []
XYs = []
lines = []

def line(x1,x2,y1,y2):
    line = plt.Line2D((x1,x2),(y1,y2), color='b', linewidth=1, zorder=0)
    lines.append(line)
    plt.gca().add_line(line)
 
plt.ion()
fig = plt.figure()    

for x in range(len(NN)):
    for y in range(NN[x]):
        node = plt.Circle((WIDTH*x+1,y+1+DIF[x]), 0.1,color='r', zorder=1)
        nodes.append(node)
        XY.append(y+1+DIF[x])
    layers.append(nodes)
    nodes = []
    XYs.append(np.array(XY))
    XY = []
    
ax = plt.gca()
ax.cla() # clear things for fresh plot   
ax.set_xlim((0, MAX*2))
ax.set_ylim((0, MAX*2))
    
for l in layers:
    for n in l:
        ax.add_patch(n)
             
for i in range(len(XYs)-1):
    for left in XYs[i]:
        x1 = i
        y1 = left
        for right in XYs[i+1]:
            x2 = i+1
            y2 = right
            line(WIDTH*x1+1, WIDTH*x2+1, y1, y2)

colors = list(['bgrcmk'][0])
w = len(colors)

plt.axis('scaled')
plt.axis('off')
plt.title( 'Representing Neural Nodes', fontsize=15 )
fig.canvas.draw()
fig.canvas.flush_events()

for l in range(len(layers)):
    for i in range(len(layers[l])):
        layers[l][i].set_width(0.2)
        layers[l][i].set_color(f'{colors[(i+l)%w]}')
        #layers[l][i].set_radius(random.randrange(1, 10)/10)
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(.01)
for l in range(len(lines)):
    lines[l].set_color(f'{colors[l%w]}')
    lines[l].set_linewidth((3*l/20)%2+.2)
    fig.canvas.draw()
    fig.canvas.flush_events()       
    time.sleep(.01)

time.sleep(2)
                      
