# RPS - Reward Punishment System

### What Problem is This Solving?
This is solving the biggest problem we have as humans, which is: How to Stay Motivated.

I talk about why we are **not** motivated at length **here** (link being added soon!). The basic idea that is relevant to this project is: Direct Rewards & Direct Punishments don't work. If you implement them, you will condition yourself like Pavlov's dog, and that is not good in the long term. There is a need for a better solution.

### A Practical Way to Stay Motivated
The solution is: don't directly associate outcomes to rewards and punishments. Make the associations loose. What this means is: motivation is created out of uncertainty. Rather than telling you:
> get "X" amount of work done to either get a reward / avoid a punishment
 
I instead say:

> The more work you do, the higher the chances that you'll be rewarded.

> The more time you waste, the higher the chances that you'll be punished
 
This approach is massively more effective, since your brain associates doing more work in general as a good thing, rather than associating doing a task as a good thing. Another advantage is that it's hard to pinpoint what exactly you did to get the reward, thus making it harder to exploit (unlike traditional deterministic rewards)

So how **exactly** does the RPS implement this? let's find out.

## Table of Contents
[Overview](#Overview)
- [Structure](#Structure)
- [Features](#Features)
- [Requirements](#Requirements)
- [Example](#Example)
 


## Overview
### Structure
Below is a UML Class Diagram that gives a high level understanding of how this system works together. 

(Picture will be inserted soon)

### Features
1. **Reward System**
- This system simply is used to randomly select the following parameters:
  - Probabilities of getting rewarded
  - Amount of Reward
  - Length of testing period.
  - Note: Does *not* randomize type of reward. You can choose your rewards.

3. **Punish System**
- This system simply is used to randomly select the following parameters:
  - Probabilities of getting punished
  - Type of Punishment
  - Amount of Punishment
  - Length of testing period.

5. **Monitor**
- This system monitors your efficiency/inefficiency progress and will ping you when you get rewarded/punished
- This system is also connected to your time data with an API. It will cross reference this to calculate probabilities 

### Requirements
numpy


### Example
