import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os, sys
import shutil

num_agents = 100
agent_state = np.zeros((10,10))
# print("Agent State =", agent_state)
# T = int(input('Please enter the maximum value the counter can assume: '))
T = 100
c_grid = np.random.randint(low=0, high=T, size=(agent_state.shape[0], agent_state.shape[1]))
# print("C Grid =", c_grid)

k = 0.5

dR = [-1, +1, 0, 0]
dC = [0, 0, +1, -1]

folder_name = "temp_data"

if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
    os.mkdir(folder_name)
else:
    os.mkdir(folder_name)

image_count = 1

filenames = []
bean_counter = 0
while (bean_counter <= 1000):
    for row in range(0,agent_state.shape[0]):
        for column in range(0,agent_state.shape[1]):
            
            c_grid[row,column] = c_grid[row,column] + 1
            print(f'Count = {bean_counter}, Row = {row}, Column = {column}, State ({row},{column}) = {(int)(agent_state[row,column])}, C = {c_grid[row,column]}')

            for i in range(0,4):
                new_row = row + dR[i]
                new_column = column + dC[i]
                
                if (new_row < 0 or new_column < 0):
                    # print("Array index negative")
                    continue

                if (new_row >= agent_state.shape[0] or new_column >= agent_state.shape[1]):
                    # print("Array out of bounds")
                    continue

                if (agent_state[new_row,new_column] == 1):
                    c_grid[row,column] = c_grid[row,column] + k * c_grid[row,column]
                
            if (c_grid[row,column] >= T):
                agent_state[row,column] = 1
                c_grid[row,column] = 0
            else:
                agent_state[row,column] = 0

    filename = f'temp_data/{image_count}.png'
    filenames.append(filename)
    image_count = image_count + 1
    # plt.axis('off')
    plt.title(f"Global Synchronization with k = {k}")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.imshow(agent_state)
    # plt.pause(0.001)
    # plt.clf()
    plt.savefig(filename,bbox_inches='tight')
    plt.close()
    bean_counter = bean_counter + 1 

images = []
for n in filenames:
    frame = PILImage.open(n)
    images.append(frame)

images[0].save('demo.gif',
            save_all=True,
            append_images=images[1:],
            duration=10,
            loop=0)