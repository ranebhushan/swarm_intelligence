# RBE 595 - Swarm Intelligence - Spring 2023
# Homework 7 - Group Size Detection
# Worcester Polytechnic Institute
# Student: BHUSHAN ASHOK RANE <barane@wpi.edu>

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os
import shutil

width = 10
height = 10

initiation_probability = 0.1

refractory_timer = 10

agents_grid = np.zeros((height,width)) 

# False = 0
# True = 1
initiated_grid = np.zeros((height,width))

size_grid = np.zeros((height,width))

# SUSCEPTIBLE = 0
# REFACTORY = 1
state_grid = np.zeros((height,width))

# Direction Vectors to explorte neighbours of any agent
dR = [-1, +1, 0, 0]
dC = [0, 0, +1, -1]

for row in range(0,agents_grid.shape[0]):
    for column in range(0,agents_grid.shape[1]):
        if(state_grid[row,column] == 0):
            for i in range(0,len(dR)):
                new_row = row + dR[i]
                new_column = column + dC[i]
