# RL Task Scheduler (DQN vs Classical Baselines)

This repository contains a discrete-time single-processor task scheduling simulator and a comparative evaluation of classical scheduling algorithms against a Deep Reinforcement Learning approach (DQN).


## Compared methods
- FCFS (First-Come First-Served)
- RR (Round Robin, quantum = 1)
- SJF (Shortest Job First)
- EDF (Earliest Deadline First)
- DQN (Deep Q-Network)

## Workloads
- Uniform (steady arrivals)
- Bursty (arrival bursts)
- Heavy-tailed (mix of short and long tasks)
- Deadline-constrained (tight deadlines)

## Metrics
- Average waiting time
- Deadline miss rate
- Throughput

## Repository structure
- `notebooks/` : End-to-end experiment pipeline in Colab
- `results/`   : Figures and tables used in the report
- `report/`    : IEEE-format report file
- `models/`    : Saved trained model checkpoints
- `src/`       : Core simulator / agent code

## How to run (Google Colab)
Open the notebooks in `notebooks/` and run them in order (setup → generation → training → evaluation → analysis).

## Authors
- Islah Haoues
- Baker Huseyin
