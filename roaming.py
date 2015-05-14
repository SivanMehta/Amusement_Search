# attempting to use monte carlo methods to answer the question posed here:
# https://www.reddit.com/r/askscience/comments/35uljq/if_i_wanted_to_randomly_find_someone_in_an/
# If I wanted to randomly find someone in an amusement park, would my odds of finding
# them be greater if I stood still or roamed around?

import random, numpy, sys
from matplotlib import pyplot as plt

# Assumptions made:
# there are two people looking for eachother
# both of them, if they are moving, are moving in a random direction each step
# each has a vision of 10 cells
# the park is a square with no obstacles

def walk(person, parkSize):
    person[0] = (abs(person[0] + random.randint(-1,1))) % (parkSize + 1)
    person[1] = (abs(person[1] + random.randint(-1,1))) % (parkSize + 1)

# this is a really lazy test, as it tests via exhaustion
def testWalk():

    # small park
    person = [5, 5]
    parkSize = 10

    for x in xrange(10000):
        walk(person, parkSize)
        assert person[0] >= 0 and person[0] <= parkSize
        assert person[1] >= 0 and person[1] <= parkSize

    # large park
    person = [25, 25]
    parkSize = 50

    for x in xrange(10000):
        walk(person, parkSize)
        assert person[0] >= 0 and person[0] <= parkSize
        assert person[1] >= 0 and person[1] <= parkSize

    # starting in corner
    person = [0, 0]
    parkSize = 50

    for x in xrange(10000):
        walk(person, parkSize)
        assert person[0] >= 0 and person[0] <= parkSize
        assert person[1] >= 0 and person[1] <= parkSize

def withinSight(person1, person2):
    return ((person1[0] - person2[0])**2 + (person1[1] - person2[1])**2) < 10

# both walking
def walkingTrial(parkSize = 100, limit = 10000):
    steps = 0

    # let's assume they start in the same place
    husband = [random.randint(1, parkSize), random.randint(1, parkSize)]
    wife = [random.randint(1, parkSize), random.randint(1, parkSize)]

    while(not withinSight(husband, wife)):
        walk(husband, parkSize)
        walk(wife, parkSize)

        steps += 1
        if steps > limit:
            return -1

    return steps

def runTrials(trialCount = 1000, parkSize = 40):
    outcomes = []

    for trial in xrange(trialCount):
        outcome = walkingTrial(parkSize)
        if outcome >= 0:
            outcomes.append(outcome)

        sys.stdout.flush()
        sys.stdout.write("\rFinished trial %d/%d" % (trial + 1, trialCount) )

    print "... done!"

    print "Median Number of Steps --> %d for a %dx%d 'park'" % (numpy.median(outcomes), parkSize, parkSize)
    plt.hist(outcomes)
    plt.show()


# testWalk()

runTrials(parkSize = 100)
