# Homework 8 - Obstacle Avoidance and Synchronization

RBE595 - Swarm Intelligence (Spring 2023)

Master of Science in Robotics Engineering at [Worcester Polytechnic Institute](https://www.wpi.edu/)

This repository is based on the following paper : [Mirollo, R. E., & Strogatz, S. H. (1990). Synchronization of pulse-coupled biological oscillators. SIAM Journal on Applied Mathematics, 50(6), 1645-1662](https://epubs.siam.org/doi/10.1137/0150098)

## Description

### Obstacle Avoidance

Avoiding obstacles is one of the most common behaviors. The aim of this exercise is to implement
an obstacle avoidance strategy for your swarm. For this exercise, you’ll use the proximity sensor and
the robot wheels.

**Proximity Sensor Labeling**

![Screenshot from 2023-06-09 16-19-27](https://github.com/ranebhushan/swarm_workspace/assets/34753789/44817d2b-dd10-4f53-8bac-9275cd467f81)

### Synchronization

Simplified implementation of algorithm to achieve global synchronization, can be summarized as :

```
init:
    state = 0
    c = random(0,T)
step:
    c = c + 1
    if(a neighbor flashed)
        c = c + k * c
    if(c >= T)
        state = 1
        c = 0
    else
        state = 0
```

In the above algorithm, `c` is an internal counter; `T` is the maximum value the counter can assume; and `k` is a constant between 0 and 1. We assume that each agent can see the neighbors on its north, east, south and west while implementing this algorithm, with setting `T` to 100.

The range-and-bearing communication system and the LEDs are used in this exercise.

## Dependencies
- OS : [Ubuntu 20.04 LTS](https://releases.ubuntu.com/20.04/)
- ARGoS : [3.0.0-beta59](https://www.argos-sim.info/core.php)
- [Buzz](https://github.com/NESTLab/Buzz.git)
- [Khepera IV Robot](https://github.com/ilpincy/argos3-kheperaiv.git)

## Usage Guidelines

1. Launch the ARGoS simulator using the terminal with the following command :

    ```
    argos3 −c hw8.argos
    ```

    The swarm of robots will be initialized in the arena with the obstacles. 

2. Open Buzz script file `hw8.bzz` in ARGoS Script Editor and run the script using the `Execute` button.

## Results

### Obstacle Avoidance

https://github.com/ranebhushan/swarm_workspace/assets/34753789/f22d3c4e-be81-4c9f-bad5-3ad2a15ac520

### Synchronization

https://github.com/ranebhushan/swarm_workspace/assets/34753789/b6d9533d-687e-44c9-bca6-664a1f110ca2
