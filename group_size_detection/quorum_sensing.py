# RBE 595 - Swarm Intelligence - Spring 2023
# Homework 7 - Group Size Detection
# Worcester Polytechnic Institute
# Student: BHUSHAN ASHOK RANE <barane@wpi.edu>

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os
import shutil
import random

Width = 10
Height = 10

P = 0.1

R = 5

signal = np.zeros((Height,Width)) 

# False = 0
# True = 1
initiated = np.zeros((Height,Width))

group_size = np.zeros((Height,Width))

# SUSCEPTIBLE = 0
# REFACTORY = 1
agent_state = np.zeros((Height,Width))

agent_done = np.zeros((Height,Width))

refractory_timer = np.zeros((Height,Width))

# Direction Vectors to explore neighbours of any agent
# 4 Neighbors
dR = [-1, 0, +1, 0]
dC = [0, +1, 0, -1]

# 8 Neighbors
# dR = [-1, -1, 0, +1, +1, +1, 0, -1]
# dC = [0, +1, +1, +1, 0, -1, -1, -1]

# Create temporary directory to save images to create a GIF
folder_name = "temp_data"
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
    os.mkdir(folder_name)
else:
    os.mkdir(folder_name)

# Variables to create a GIF 
image_count = 1
filenames = []

# Initialize a counter to repeat 'n' number of times
bean_counter = 0

while (np.sum(initiated) < (Height*Width)):

    for row in range(0,Height):
        for column in range(0,Width):
            print(f'Counter = {bean_counter}, Max. Group Size = {np.amax(group_size)}, Group Size Sum = {np.sum(group_size)}', end='\r')

            # Check whether state is susceptible
            if(agent_state[row,column] == 0):

                # Explore neighbors
                for i in range(0,len(dR)):
                    new_row = row + dR[i]
                    new_column = column + dC[i]

                    # Check if the neighbours are valid or not 
                    if (new_row < 0 or new_column < 0):
                        # print("Array index negative")
                        continue

                    if (new_row >= agent_state.shape[0] or new_column >= agent_state.shape[1]):
                        # print("Array out of bounds")
                        continue

                    # Check if the neighbor signalled
                    if (signal[new_row,new_column] == 1):
                        signal[row,column] = 1
                        agent_state[row,column] = 1
                        refractory_timer[row,column] = R
                        group_size[row,column] += 1
                        break

                    elif ((initiated[row,column] == 0) and (random.random() < P)):
                        signal[row,column] = 1
                        agent_state[row,column] = 1
                        refractory_timer[row,column] = R
                        initiated[row,column] = 1
                        group_size[row,column] += 1
                        break
                        
                    else:
                        pass

            else:
                signal[row,column] = 0
                refractory_timer[row,column] -= 1
                if (refractory_timer[row,column] <= 0):
                    agent_state[row,column] = 0
                    refractory_timer[row,column] = 0
    
    bean_counter += 1

    # Store sequential images in the loop for GIF  
    filename = f'temp_data/{image_count}.png'
    filenames.append(filename)
    image_count = image_count + 1
    plt.title(f"Group Size Detection")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.imshow(signal)
    plt.savefig(filename,bbox_inches='tight')
    plt.close()

print(f'Counter = {bean_counter}, Max. Group Size = {np.amax(group_size)}, Group Size Sum = {np.sum(group_size)}')

# Read and Open the saved images 
images = []
for n in filenames:
    frame = PILImage.open(n)
    images.append(frame)

# Create GIF
images[0].save(f'signal.gif',
            save_all=True,
            append_images=images[1:],
            duration=10,
            loop=0)