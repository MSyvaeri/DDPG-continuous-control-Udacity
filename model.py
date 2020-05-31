#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import torch.nn.functional as F


#### Implemenation of a Duelling architecture

class Actor(nn.Module):

    def __init__(self, state_size, action_size, seed, size_1=64, size_2=64, size_3=64):
        
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.action_size=action_size
        self.dense_1 = nn.Linear(state_size, size_1)
        self.dense_2 = nn.Linear(size_1, size_2)
        self.dense_3 = nn.Linear(size_2, size_3)

        
 
        self.dense_4 = nn.Linear(size_3, action_size)
        


        

    def forward(self, state):
        x=self.dense_1(state)
        x=F.relu(x)
        x=self.dense_2(x)
        x=F.relu(x)
        x=self.dense_3(x)
        x=F.relu(x)
        x=self.dense_4(x)
        
        return F.tanh(x)

    
class Critic(nn.Module):

    def __init__(self, state_size, action_size, seed, size_1=64, size_2=64):
        
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.action_size=action_size
        self.dense_1 = nn.Linear(state_size+action_size, size_1)
        self.dense_2 = nn.Linear(size_1, size_2)
        self.dense_3 = nn.Linear(size_2, 1)
        


    def forward(self, state,action):
        x=torch.cat((state, action), dim=1)
        x=self.dense_1(x)
        x=F.relu(x)
        
        x=self.dense_2(x)
        x=F.relu(x)
        
        
        return self.dense_3(x)


# In[ ]:




