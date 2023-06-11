# Homework 8 - Obstacle Avoidance and Synchronization

[RBE595 - Swarm Intelligence](https://www.wpi.edu/sites/default/files/inline-image/Departments-Programs/Robotics-Engineering/RBE.Special.%20Topics.%20Courses_%20Spring.2023.pdf) (Spring 2023)

[Master of Science](https://www.wpi.edu/academics/study/robotics-engineering-ms) in [Robotics Engineering](https://www.wpi.edu/academics/departments/robotics-engineering) at [Worcester Polytechnic Institute](https://www.wpi.edu/)

This repository is based on the following paper : [Mirollo, R. E., & Strogatz, S. H. (1990). Synchronization of pulse-coupled biological oscillators. SIAM Journal on Applied Mathematics, 50(6), 1645-1662](https://epubs.siam.org/doi/10.1137/0150098)

## Description

### Obstacle Avoidance

Avoiding obstacles is one of the most common behaviors. The aim of this exercise is to implement
an obstacle avoidance strategy for your swarm. For this exercise, you’ll use the proximity sensor and
the robot wheels.

**Proximity Sensor Labeling**

![Screenshot from 2023-06-09 16-19-27](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/1f04c116-f628-4c6a-80a2-a60c1659141b)

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
- ARGoS Simulator : [3.0.0-beta59](https://www.argos-sim.info/core.php)
- Programming Language : [Buzz](https://github.com/NESTLab/Buzz.git)
- [Buzz Wiki](https://the.swarming.buzz/wiki/doku.php?id=start)
- [Buzz Cheatsheet](https://the.swarming.buzz/wiki/doku.php?id=buzz_syntax_cheatsheet)
- [ARGoS-Buzz Integration](https://the.swarming.buzz/wiki/doku.php?id=buzz_argos)
- [Khepera IV Robot](https://github.com/ilpincy/argos3-kheperaiv.git)
- [Khepera IV Robot Commands](https://the.swarming.buzz/wiki/doku.php?id=buzz_kh4)

## Usage Guidelines

1. Launch the ARGoS simulator using the terminal with the following command :

    ```
    argos3 −c hw8.argos
    ```

    The swarm of robots will be initialized in the arena with the obstacles. 

2. Open Buzz script file `hw8.bzz` in ARGoS Script Editor and run the script using the `Execute` button.

## Results

### Obstacle Avoidance

https://github.com/ranebhushan/swarm_intelligence/assets/34753789/f684b379-3e1a-4a26-8b57-6bd3c2361fba

### Synchronization

https://github.com/ranebhushan/swarm_intelligence/assets/34753789/1f48b68e-50ca-43c8-81e0-aab858701303
