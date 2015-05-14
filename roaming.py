# attempting to use monte carlo methods to answer the question posed here:
# https://www.reddit.com/r/askscience/comments/35uljq/if_i_wanted_to_randomly_find_someone_in_an/
# If I wanted to randomly find someone in an amusement park, would my odds of finding
# them be greater if I stood still or roamed around?

import random

# Assumptions made:
# there are two people looking for eachother
# both of them, if they are moving, are moving in a random direction each step
# each has a vision of 1/10th of the overall size of the "park"
# the park is a square with no obstacles

def walkingTrial([parkSize = 10]):
    number = 1

    # let's assume they start in the same place
    husband = [random.randint(1, parkSize), random.randint(1, parkSize)]
    wife = [random.randint(1, parkSize), random.randint(1, parkSize)]

    return number