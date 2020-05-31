# DDPG-continuous-control-Udacity

Project: Continuous-control

Introduction:

In this repository, we solve the environment “Reacher” with a DDPG-agent. In this environment, the agent controlls a double-jointed robotic arm, the task is to reach a moving goal position. For each time step the robotic arm is in the location, it will get a reward of +0.1.
Thus, the goal is to stay as long as possible in the goal position. The environment is solved if the agent reaches an average reward of +30 over consecutive 100 attempts.

The state space has 33 dimensions and contains position, rotation, velocity, and angular velocities of the arm. Each action is a vector of 4 dimensions, corresponding to rotations of the joints. Each number must be between -1 and +1.

