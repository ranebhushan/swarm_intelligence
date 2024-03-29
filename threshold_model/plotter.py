import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time

# Provide datafile path
datafile_path = os.path.join(os.path.dirname(__file__), 'data_normal.dat')
print(datafile_path)

# Read data from datafile
file = open(datafile_path)
data = []
for line in file:
    data.append(line.split())
data = np.array(data, dtype=float)

# Define number of robots
NUM_ROBOTS = 20

# Sort data by time step
robot = np.empty(NUM_ROBOTS, dtype=object)
for i in range(NUM_ROBOTS):
    if i == 0:
        robot[0] = data[::NUM_ROBOTS]
    else:
        robot[i] = (data[i::NUM_ROBOTS])

# Define lambda functions to extract data
get_time = lambda lists : list(map(lambda x: x[0], lists))
get_task = lambda lists : list(map(lambda x: x[2], lists))
get_threshold0 = lambda lists : list(map(lambda x: x[3], lists))
get_threshold1 = lambda lists : list(map(lambda x: x[4], lists))

# Plot graph of time step vs task
for i in range(NUM_ROBOTS):
    plt.plot(get_time(robot[i]), get_task(robot[i]), label='robot'+str(i))
plt.xlim([0, int(max(data[:,0]))])
plt.ylim([int(float(min(data[:,2])))-0.5, int(float(max(data[:,2])))+0.5])
plt.xticks(np.arange(int(0), int(float(max(data[:,0]))), 100), fontsize=16)
plt.yticks(np.arange(int(float(min(data[:,2])))-0.5, int(float(max(data[:,2])))+0.5, 0.5), fontsize=16)
plt.title("Time Step vs Task", fontsize=20)
plt.xlabel("Time Step", fontsize=18)
plt.ylabel("Task", fontsize=18)
plt.legend()
plt.show()

# Plot graph of time step vs threshold0
for i in range(NUM_ROBOTS):
    plt.plot(get_time(robot[i]), get_threshold0(robot[i]), label='robot'+str(i))
plt.xlim([0, max(data[:,0])])
plt.ylim([0, max(data[:,3])])
plt.xticks(np.arange(int(0), int(float(max(data[:,0]))), 100), fontsize=16)
plt.yticks(np.arange(int(0), int(float(max(data[:,3])))+100, 100), fontsize=16)
plt.title("Time Step vs Threshold 0", fontsize=20)
plt.xlabel("Time Step", fontsize=18)
plt.ylabel("Threshold 0", fontsize=18)
plt.legend()
plt.show()

# Plot graph of time step vs threshold1
for i in range(NUM_ROBOTS):
    plt.plot(get_time(robot[i]), get_threshold1(robot[i]), label='robot'+str(i))
plt.xlim([0, max(data[:,0])])
plt.ylim([0, max(data[:,4])])
plt.xticks(np.arange(int(0), int(float(max(data[:,0]))), 100), fontsize=16)
plt.yticks(np.arange(int(0), int(float(max(data[:,4])))+100, 100), fontsize=16)
plt.title("Time Step vs Threshold 1", fontsize=20)
plt.xlabel("Time Step", fontsize=18)
plt.ylabel("Threshold 1", fontsize=18)
plt.legend()
plt.show()