# RBE 595 - Swarm Intelligence - Spring 2023
# Homework 6 - Coupled Oscillators
# Worcester Polytechnic Institute
# Student: BHUSHAN ASHOK RANE <barane@wpi.edu>

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os
import shutil
import datetime

# Initialize the agent states to 0 
agent_state = np.zeros((10,10))
# print("Agent State =", agent_state)

# Taking user input for value of T
# T = int(input('Please enter the maximum value the counter can assume: '))
T = 100

c_grid = np.random.randint(low=0, high=T, size=(agent_state.shape[0], agent_state.shape[1]))
# print("C Grid =", c_grid)

# Initialize the value of k
k = 0.9

# Direction Vectors to explorte neighbours of any agent
dR = [-1, +1, 0, 0]
dC = [0, 0, +1, -1]

# Create temporary directory to save images to create a GIF
folder_name = f'temp_data-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
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

while (bean_counter <= 1500):
    for row in range(0,agent_state.shape[0]):
        for column in range(0,agent_state.shape[1]):
            
            c_grid[row,column] = c_grid[row,column] + 1
            print(f'Count = {bean_counter}, Row = {row}, Column = {column}, State ({row},{column}) = {(int)(agent_state[row,column])}, C = {c_grid[row,column]}')

            for i in range(0,4):
                new_row = row + dR[i]
                new_column = column + dC[i]
                
                # Check if the neighbours are valid or not 
                if (new_row < 0 or new_column < 0):
                    # print("Array index negative")
                    continue

                if (new_row >= agent_state.shape[0] or new_column >= agent_state.shape[1]):
                    # print("Array out of bounds")
                    continue

                # Update 'c' if any of the neighbour agent flashes
                if (agent_state[new_row,new_column] == 1):
                    c_grid[row,column] = c_grid[row,column] + k * c_grid[row,column]
                
            # If the counter exceeds the maximum value, update the agent state and reset the counter
            if (c_grid[row,column] >= T):
                agent_state[row,column] = 1
                c_grid[row,column] = 0
            else:
                agent_state[row,column] = 0

    # Store sequential images in the loop for GIF  
    filename = f'{folder_name}/{image_count}.png'
    filenames.append(filename)
    image_count = image_count + 1
    plt.title(f"Global Synchronization with k = {k}")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.imshow(agent_state)
    # plt.pause(0.001)
    # plt.clf()
    plt.savefig(filename,bbox_inches='tight')
    plt.close()
    bean_counter = bean_counter + 1 

# Read and Open the saved images 
images = []
for n in filenames:
    frame = PILImage.open(n)
    images.append(frame)

# Create GIF
images[0].save(f'k={k}.gif',
            save_all=True,
            append_images=images[1:],
            duration=10,
            loop=0)

shutil.rmtree(folder_name)