# Homework 3 - The Schelling Model

[RBE595 - Swarm Intelligence](https://www.wpi.edu/sites/default/files/inline-image/Departments-Programs/Robotics-Engineering/RBE.Special.%20Topics.%20Courses_%20Spring.2023.pdf) (Spring 2023)

[Master of Science](https://www.wpi.edu/academics/study/robotics-engineering-ms) in [Robotics Engineering](https://www.wpi.edu/academics/departments/robotics-engineering) at [Worcester Polytechnic Institute](https://www.wpi.edu/)
## Description
- The world is a 50 × 50 grid, for a total of `G` = 2500 cells.
- The population `P` is expressed as a fraction of the cells. `P` = {0.6, 0.8}.
- The agents are always 50% `X` and 50% `O`.
- The satisfaction threshold is set to `t` = {3, 4, 5}.
    - Run 10 simulations with all the agents having `t` = 3.
    - Run 10 simulations with all the agents having `t` = 4.
    - Run 10 simulations with 80% of the agents of each type having `t` = 3 and the rest `t` = 5.
- Agents are updated according to the cell they occupy, left-to-right, top-to-bottom. Start at the top-left corner in the grid, move left-to-right along the first row, and update all the agents you encounter. Once done with the row, move down to the leftmost cell of the second row, and repeat the above steps.
- Unsatisfied agents move to the closest cell that makes them satisfied. Use 8-distance to find the closest cell.
- You can run the simulation for as many steps as you see fit. A good value is 1000 steps.

## Dependencies
- OS : [Ubuntu 20.04 LTS](https://releases.ubuntu.com/20.04/)
- Python : [3.8.10](https://www.python.org/downloads/release/python-3810/)

## Usage Guidelines
1. Navigate to the directory `src`.
2. Run the given python file `python schelling_model.py` or `python3 schelling_model.py`.

## Results

![2023-01-30--20-12-30 P=0 6 t=3 0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/258b1e3f-71ae-4f80-8420-aa7bbcec040c)

![2023-01-30--20-15-27 P=0 6 t=4 0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/5efc4672-5385-4204-8c9c-18778eb6d48a)

![2023-01-30--20-19-55 P=0 8 t=3 0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/ecfaa506-405e-4f7e-b0eb-12289dc4a3fc)

![2023-01-30--20-25-18 P=0 8 t=4 0](https://github.com/ranebhushan/swarm_intelligence/assets/34753789/dd9ec370-c151-4579-a615-7cbf4b2cb252)

## References
- [Schelling's Segregation Model](http://www.natureincode.com/code/various/schelling.html)
- [Schelling's Model of Segregation](http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/)
