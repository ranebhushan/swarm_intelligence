# Homework 6 - Coupled Oscillators

[RBE595 - Swarm Intelligence](https://www.wpi.edu/sites/default/files/inline-image/Departments-Programs/Robotics-Engineering/RBE.Special.%20Topics.%20Courses_%20Spring.2023.pdf) (Spring 2023)

[Master of Science](https://www.wpi.edu/academics/study/robotics-engineering-ms) in [Robotics Engineering](https://www.wpi.edu/academics/departments/robotics-engineering) at [Worcester Polytechnic Institute](https://www.wpi.edu/)

This repository is based on the following paper : [Mirollo, R. E., & Strogatz, S. H. (1990). Synchronization of pulse-coupled biological oscillators. SIAM Journal on Applied Mathematics, 50(6), 1645-1662](https://epubs.siam.org/doi/10.1137/0150098)

## Description

This repository contains simplified implementation of algorithm to achieve global synchronization, which can be summarized as :

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

## Dependencies
- OS : [Ubuntu 20.04 LTS](https://releases.ubuntu.com/20.04/)
- Python : [3.8.10](https://www.python.org/downloads/release/python-3810/)
- NumPy : [v1.22.3](https://numpy.org/)
- Matplotlib : [3.6.3](https://matplotlib.org/stable/index.html)
- Pillow : [9.4.0](https://pillow.readthedocs.io/en/stable/)

## Usage Guidelines

Run the python script in this directory using : `python coupled_oscillators.py`

## Results

![k=0 5](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/66778fd3-88f9-45d2-b8a7-394e960ff6d6)
