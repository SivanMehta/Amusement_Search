# Finding people in an Amusment Park

Based on the /r/askscience post found [here](https://www.reddit.com/r/askscience/comments/35uljq/if_i_wanted_to_randomly_find_someone_in_an/). I choose to simply look at the results of a Monte Carlo Simulation for each. The question asked was "If I wanted to randomly find someone in an amusement park, would my odds of finding them be greater if I stood still or roamed around?".

According to a simulation for a 100x100 "park" and a 10-unit sight radius, **roaming around would be the better option**. 

According to the simulation, roaming around produces a median step requirement of 2815 steps, while having 1 person sit still produces a median step requirement of 3475 steps.

In addition to answering the question, I also wanted to explore a useful way of displaying the data, as well as efficiently doing a monte carlo simulation, which lends itself perfectly to being multithreaded

### Running the Test
```bash
$ python roaming.py
Started 16 threads... all threads started!
Batch 10 of 10 completed... Done!
Median Number of Steps --> 2799 for a 100x100 'park'
```

This trail is expected to run for about 1.5 minutes

```bash
$ time python roaming.py > out.log
real	1m27.551s
user	0m45.280s
sys		0m17.336s
```

### Requirements
```shell
$ python --version
Python 2.7.8
$ pip freeze | grep psutil
psutil==3.0.1
```
