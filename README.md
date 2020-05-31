# DDPG-continuous-control-Udacity

Project: Continuous-control

Introduction:

In this repository, we solve the environment “Reacher” with a DDPG-agent. In this environment, the agent controlls a double-jointed robotic arm, the task is to reach a moving goal position. For each time step the robotic arm is in the location, it will get a reward of +0.1.
Thus, the goal is to stay as long as possible in the goal position. The environment is solved if the agent reaches an average reward of +30 over consecutive 100 attempts.

The state space has 33 dimensions and contains position, rotation, velocity, and angular velocities of the arm. Each action is a vector of 4 dimensions, corresponding to rotations of the joints. Each number must be between -1 and +1.

The agent can be trained by running the jupyter notebook “Continuous_Control.ipynb”, while the information about the agent are stored in the file “ddpg_agent.py”. The neural network is stored in the file “model.py”, while the weights of a trained network are in the file “actor_model.pt” and “critic_model.pt”.

In this file, we are using an environment where we get the information from 20 agents acting parallel.

Needed Files:

To use the code you have to download "Run.ipynb" and the files “ddpg_agent.py” and “model.py”. Additionally, you have to download the environment "Banana":

    Linux: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip
    Mac OSX: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip
    Windows (32-bit): https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip
    Windows (64-bit): https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip
