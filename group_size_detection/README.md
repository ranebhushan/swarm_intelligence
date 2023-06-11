# Homework 7 - Group Size Detection

RBE595 - Swarm Intelligence (Spring 2023)

Master of Science in Robotics Engineering at [Worcester Polytechnic Institute](https://www.wpi.edu/)

## Description

This repository contains an implementation of a simple algorithm for calculating a _very rough estimate_ of the size of a group of agents in a completely decentralized manner. This algorithm is called **[quorum sensing](https://en.wikipedia.org/wiki/Quorum_sensing)** and it is used by certain bacteria to know when to launch an attack on the body of the host.

The algorithm works as follows:

- The agents are the cells of a `W` × `H` grid. Consider the cases `5×5`, `10×10`, `20×20`.
- The agents do not know how many they are (that’s what they need to estimate!), nor their position in the grid.
- The simulation proceeds in steps in the same fashion as the synchronization algorithm in [coupled_oscillators](https://github.com/ranebhushan/swarm_workspace/tree/main/coupled_oscillators).
- At any time, the agents can be either `susceptible` or `refractory`.
- At any time, a `susceptible` agent has a _probability_ `P` of initiating a “signal wave” by emitting a signal. An agent can initiate a signal only once throughout the duration of an experiment.
- Upon receiving a signal, any `susceptible` neighbor emits a signal too, thus continuing the “signal wave”.
- Any time it emits a signal (initiated or forwarded), the agent enters the `refractory` state. In this state, the agent ignores any received signal and cannot initiate a signal. This state lasts for `R` steps, after which the agent swicthes back to `susceptible`.
- Any time it emits a signal (initiated or forwarded), the agent increases by 1 its estimate of the group size. The group size is initialized to 0 for all agents.
- In principle, the simulation ﬁnishes when all the agents have signalled. However, the agents have no way to know this; therefore, any agent considers itself **done** when it has received no signal for `1/P` continuous steps. When all agents consider themselves “done”, the simulation ends.

The above algorithm can be summarized as :

```
input:
    W = grid width [int]
    H = grid height [int]
    P = initiation probability [float]
    R = refractorytimer [int]

init:
    initiated = false [boolean]
    size = 0 [int]
    state = Susceptible

step:
    if (state == Susceptible)
        if (neighbor signalled)
            emit signal
            state = Refractory
            refractorytimer = R
            size = size + 1
        elif (not initiated) and (random() < P)
            emit signal
            state = Refractory
            refractorytimer = R
            initiated = true
            size = size + 1
        endif
    else
        refractorytimer = refractorytimer - 1
        if (refractorytimer <= 0)
            state = Susceptible
        endif
    endif
```

## Dependencies
- OS : [Ubuntu 20.04 LTS](https://releases.ubuntu.com/20.04/)
- Python : [3.8.10](https://www.python.org/downloads/release/python-3810/)
- NumPy : [v1.22.3](https://numpy.org/)
- Matplotlib : [3.6.3](https://matplotlib.org/stable/index.html)
- Pillow : [9.4.0](https://pillow.readthedocs.io/en/stable/)

## Usage Guidelines

Run the python script in this directory using : `python quorum_sensing.py`

## Results

![signal](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/19d54946-2d89-4381-8b0a-dad72fba80dd)
