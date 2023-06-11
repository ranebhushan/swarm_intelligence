# RBE595 - Swarm Intelligence

Repository for [RBE595 - Swarm Intelligence](https://www.wpi.edu/sites/default/files/inline-image/Departments-Programs/Robotics-Engineering/RBE.Special.%20Topics.%20Courses_%20Spring.2023.pdf) Course Assignments (Spring 2023)

[Master of Science](https://www.wpi.edu/academics/study/robotics-engineering-ms) in [Robotics Engineering](https://www.wpi.edu/academics/departments/robotics-engineering) at [Worcester Polytechnic Institute](https://www.wpi.edu/)

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

![2023-01-30--20-25-18 P=0 8 t=4 0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/649c465b-a2ae-4c6c-a52b-48a818f9507d)

- [Coupled Oscillators](coupled_oscillators/)

![k=0 5](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/701002d0-17cb-4778-8795-949d2c6fed6b)

- [Group Size Detection](group_size_detection/)

![signal](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/83209b6c-2d5e-4797-b21e-2d02e93dc9c3)

- [Obstacle Avoidance](obstacle_avoidance/)

https://github.com/ranebhushan/swarm_intelligence/assets/34753789/f1d4acf4-69e5-45ec-8d78-2ca0fa6d08fb

- [Threshold Model](threshold_model/)

![normal_time_threshold0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/d2f468f9-71a3-4bc8-9cc4-5a71fdd55016)

![normal_time_threshold1](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/4432838c-69ba-4a9e-a508-34be8f5baf2e)
