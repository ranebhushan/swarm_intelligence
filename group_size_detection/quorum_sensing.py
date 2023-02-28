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

# Initialize grid dimensions
width = 20
height = 20

# Signal Probability
probability = 0.01

# Refractory Timer for each agent
R = 10

# Define the number of neighbors (4 or 8)
num_neighbors = 8

# Initialize signal matrix
# Signalled - 1, Not signalled - 0 
signal = np.zeros((height,width)) 

# False = 0
# True = 1
initiated = np.zeros((height,width))

group_size = np.zeros((height,width))

# SUSCEPTIBLE = 0
# REFACTORY = 1
agent_state = np.zeros((height,width))

# Initialize matrix to check if agent considers itself done
agent_done = np.zeros((height,width))

# Initialize matrix for refractory timer of each agent
refractory_timer = np.zeros((height,width))

# Initialize matrix for idle steps of each agent
agent_done_steps = np.zeros((height,width))

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

# Initialize flag to run simulation
simulation_complete_flag = False

# Counter to note algorithm iterations 
bean_counter = 0

print(f'W = {width}, H = {height}, P = {probability}, R = {R}, Neighbors = {num_neighbors}')

while simulation_complete_flag == False:
    for row in range(0,height):
        for column in range(0,width):
            print(f'Counter = {bean_counter}, Max. Group Size = {np.amax(group_size)}, Sum Agent Done = {np.sum(agent_done)}', end='\r')
            # Check whether state is Susceptible
            if(agent_state[row,column] == 0):

                # Explore 4 Neighbors
                if (num_neighbors == 4):
                    neighbor = (signal[max(row-1,0),column] or signal[min(height-1,row+1),column] or signal[row,max(column-1,0)] or signal[row,min(width-1,column+1)])

                # Explore 8 Neighbors
                if (num_neighbors == 8):
                    neighbor = (signal[max(row-1,0),column] or signal[min(height-1,row+1),column] or signal[row,max(column-1,0)] or signal[row,min(width-1,column+1)] or signal[max(row-1,0),max(column-1,0)] or signal[max(row-1,0),min(width-1,column+1)] or signal[min(height-1,row+1),max(column-1,0)] or signal[min(height-1,row+1),min(width-1,column+1)])

                # Check neighbors
                if (neighbor):
                    # Emit Signal
                    signal[row,column] = 1
                    agent_state[row,column] = 1
                    refractory_timer[row,column] = R
                    group_size[row,column] += 1
                    agent_done_steps[row,column] = 0

                elif ((initiated[row,column] == 0) and (random.random() < probability)):

                    # Emit signal
                    signal[row,column] = 1
                    agent_state[row,column] = 1
                    refractory_timer[row,column] = R
                    initiated[row,column] = 1
                    group_size[row,column] += 1
                    agent_done_steps[row,column] = 0

                # Increment steps if NO Signal is received    
                else:
                    agent_done_steps[row,column] += 1

            else:
                signal[row,column] = 0
                refractory_timer[row,column] -= 1
                if (refractory_timer[row,column] <= 0):
                    agent_state[row,column] = 0
                    refractory_timer[row,column] = 0

                # Explore 4 Neighbors
                if (num_neighbors == 4):
                    neighbor = (signal[max(row-1,0),column] or signal[min(height-1,row+1),column] or signal[row,max(column-1,0)] or signal[row,min(width-1,column+1)])

                # Explore 8 Neighbors
                if (num_neighbors == 8):
                    neighbor = (signal[max(row-1,0),column] or signal[min(height-1,row+1),column] or signal[row,max(column-1,0)] or signal[row,min(width-1,column+1)] or signal[max(row-1,0),max(column-1,0)] or signal[max(row-1,0),min(width-1,column+1)] or signal[min(height-1,row+1),max(column-1,0)] or signal[min(height-1,row+1),min(width-1,column+1)])

                # Check neighbors
                if (neighbor):
                    agent_done_steps[row,column] = 0
                
                # Increment steps if NO Signal is received 
                else:
                    agent_done_steps[row, column] += 1

            # any agent considers itself “done” when it has received 
            # NO signal for 1/P continuous steps
            if (agent_done_steps[row,column] == (1/probability)):
                agent_done[row,column] = 1

            bean_counter += 1

    # Check if all agents considers itself done
    if (np.sum(agent_done) == (height*width)):
        simulation_complete_flag = True
        break
    
    # Store sequential images in the loop for GIF  
    # filename = f'temp_data/{image_count}.png'
    # filenames.append(filename)
    # image_count = image_count + 1
    # plt.title(f"Group Size Detection")
    # plt.xlabel("Columns")
    # plt.ylabel("Rows")
    # plt.imshow(signal)
    # plt.savefig(filename,bbox_inches='tight')
    # plt.close()

print(f'Counter = {bean_counter}, Max. Group Size = {np.amax(group_size)}, Sum Agent Done = {np.sum(agent_done)}')
print("-"*80)

# # Read and Open the saved images 
# images = []
# for n in filenames:
#     frame = PILImage.open(n)
#     images.append(frame)

# # Create GIF
# images[0].save(f'signal.gif',
#             save_all=True,
#             append_images=images[1:],
#             duration=10,
#             loop=0)