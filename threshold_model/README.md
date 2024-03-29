# Homework 9 - Threshold Model

[RBE595 - Swarm Intelligence](https://www.wpi.edu/sites/default/files/inline-image/Departments-Programs/Robotics-Engineering/RBE.Special.%20Topics.%20Courses_%20Spring.2023.pdf) (Spring 2023)

[Master of Science](https://www.wpi.edu/academics/study/robotics-engineering-ms) in [Robotics Engineering](https://www.wpi.edu/academics/departments/robotics-engineering) at [Worcester Polytechnic Institute](https://www.wpi.edu/)
## Description

In this exercise, the threshold model of Theraulaz *et al.* is implemented. The model is based on the assumption that the probability of a robot switching its state from inactive to active is proportional to the number of active robots in its neighborhood. The model is implemented in ARGoS simulator using Buzz language.

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

1. To compile the code, run the following commands in your terminal:
    ```
    cd threshold_model
    mkdir build
    cd build
    cmake ..
    make
    ```

2. Launch the ARGoS simulator using the terminal (make sure to be in the `threshold_model` directory) with the following command :

    ```
    argos3 −c threshold_model.argos
    ```

    The swarm of robots will be initialized in the arena with the obstacles. 

3. Open Buzz script file `threshold_model.bzz` in ARGoS Script Editor and run the script using the `Execute` button.

## Results

For the first experiment, thresholds and spontaneous switching probability are initialized to fixed value of 500 and 0.2 respectively. Some robots specialize towards task 0 while the remaining robots tend to converge towards task 1. The robots tend to converge within simulation time of 1500 units. However, there is an exception as seen in Time vs Threshold1 graph where one of the robots does not specialize even in 1500 units. This is because the robot is not able to find any active robot in its neighborhood and hence it does not switch its state from inactive to active. The robot is stuck in inactive state and hence it does not specialize towards any task.

![normal_time_threshold0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/60825353-9058-4207-8de8-50d546266e8e)

![normal_time_threshold1](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/86259da9-3de5-4dc3-8553-bfb236b621bb)

For the second experiment, uniform probability distribution `math.rng.uniform()` is used to spontaneous switching probability `P` and observed the following graphs which vary a little bit from the above initial graphs. Here, it can be observed that the some of the robots that were initialized with thresholds less than 500, tend to converge towards task 0 with the threshold decreasing from initial value and then suddenly increasing towards 1000 in a simulation time of 1700 units. Also, none of the robots specialized in task 1 and the task 1 threshold reduced to 0 as the simulation ended.

![uniformP_time_threshold0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/84f6be7c-9bcc-4bb3-bbc5-4168aaecb110)

![uniformP_time_threshold1](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/c440fd75-d0f3-4d08-ae22-020d8efe838d)

For the third experiment, the task thresholds were initialized uniformly between 0 and 1000 using `math.rng.uniform()`. Some robots that were initialized with threshold greater than 700 for task 0, immediately tend to specialize in task 0, whereas the other robots initialized with threshold less than 300, has their threshold reduced to 0 immediately. Also, 2 of the robots specialized in task 0 initially with threshold increasing towards 1000 and dropping to 0 as the simulation ended in time of 1600 units. Also, 1 of the robots took a longer time to reach the highest threshold and specialize in that task. Similarly, some robots that were initialized with threshold greater than 900 for task 1, immediately tend to specialize in task 1, whereas the other robots initialized with threshold less than 200, has their threshold reduced to 0 immediately. Very few robots (5) specialized in task 1 with their threshold reaching highest value in stipulated simulation time.

![uniformTH_time_threshold0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/39ad8a15-9057-42bc-b5d7-0daa3e360e24)

![uniformTH_time_threshold1](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/0ff3f272-05cd-4111-a116-318c16b0303c)
