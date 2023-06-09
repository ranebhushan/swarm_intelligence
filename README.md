# RBE595 - Swarm Intelligence Coursework

Repository for RBE595 - Swarm Intelligence Course Assignments (Spring 2023)

Master of Science in Robotics Engineering at [Worcester Polytechnic Institute](https://www.wpi.edu/)

## Description

This course covers a wide range of topics in swarm intelligence, including mathematical, computational, and biological aspects. The course is organized in four parts. In the first part, the students learn about complex systems and the basic concepts of self-organization, such as positive  and negative feedback, symmetry breaking, and emergence. The second part concerns several types of network models, such as information cascades, epidemics and voting. The instructor illustrates a diverse collection of self-organized systems in nature, finance, and technology that concretize these concepts. The third part is dedicated to swarm robotics, and will cover common swarm algorithms for task allocation, collective motion, and collective decision-making. The fourth and final part covers optimization algorithms inspired by swarm intelligence, namely ant colony optimization and particle swarm optimization. The course blends theory and practice, challenging the students to learn by implementing the algorithms discussed in class. 

## Dependencies

- OS : [Ubuntu 20.04 LTS](https://releases.ubuntu.com/20.04/)
- Python : [3.8.10](https://www.python.org/downloads/release/python-3810/)
- ARGoS Simulator : [3.0.0-beta59](https://www.argos-sim.info/core.php)
- Programming Language : [Buzz](https://github.com/NESTLab/Buzz.git)

## Setup

In order to setup the repository and virtual environment locally on your system, open a new terminal and follow the instructions below:

```
git clone https://github.com/ranebhushan/swarm_intelligence.git
cd swarm_intelligence
python -m venv swarm_env
source swarm_env/bin/activate
pip install -r requirements.txt
```

## Course Assignments

- [The Schelling Model](schelling_model/)
- [Coupled Oscillators](coupled_oscillators/)
- [Group Size Detection](group_size_detection/)
- [Obstacle Avoidance](obstacle_avoidance/)
- [Threshold Model](threshold_model/)