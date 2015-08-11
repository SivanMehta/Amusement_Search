# attempting to use monte carlo methods to answer the question posed here:
# https://www.reddit.com/r/askscience/comments/35uljq/if_i_wanted_to_randomly_find_someone_in_an/
# If I wanted to randomly find someone in an amusement park, would my odds of finding
# them be greater if I stood still or roamed around?

# for doing calculations and plotting
import random, numpy
from matplotlib import pyplot as plt

# for doing trails in parallel
from Queue import Queue
from threading import Thread

# for counting cores
import psutil

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

    # let's assume they start in random places
    husband = [random.randint(1, parkSize), random.randint(1, parkSize)]
    wife = [random.randint(1, parkSize), random.randint(1, parkSize)]

    while(not withinSight(husband, wife)):
        walk(husband, parkSize)
        walk(wife, parkSize)

        steps += 1
        if steps > limit:
            return -1

    return steps

# one walking (let's say the husband gets lost and the wife has to go find him)
def sittingTrial(parkSize = 100, limit = 10000):
    steps = 0

    # let's assume they start in random places
    husband = [random.randint(1, parkSize), random.randint(1, parkSize)]
    wife = [random.randint(1, parkSize), random.randint(1, parkSize)]

    while(not withinSight(husband, wife)):
        # walk(husband, parkSize)
        walk(wife, parkSize)

        steps += 1
        if steps > limit:
            return -1

    return steps

def runTrials(trialCount = 1000, parkSize = 40):

    q = Queue(maxsize=0)
    # generally recommended to have a max of 4 threads per core (according to by boss)
    num_threads = psutil.cpu_count() * 4
    outcomes = []

    def trail_thread(q):
        while True:
            print q.get()
            outcome = walkingTrial(parkSize)
            if outcome >= 0:
                outcomes.append(outcome)
            q.task_done()

    # start the threads
    for i in xrange(num_threads):
        worker = Thread(target = trail_thread, args = (q,))
        worker.setDaemon(True)
        worker.start()
        print "started %d threads" % (i + 1)

    # start the trails
    for i in xrange(trialCount):
        q.put(i)

    # wait for all threads to be done
    q.join()

    print "Median Number of Steps --> %d for a %dx%d 'park'" % (numpy.median(outcomes), parkSize, parkSize)
    plt.hist(outcomes, bins = 20)
    plt.ylabel("Frequency")
    plt.xlabel("Steps Taken")
    plt.title("Steps Taken while looking in a %i x %i 'park'" % (parkSize, parkSize))
    plt.grid(True)
    plt.show()


# testWalk()

runTrials(parkSize = 100, trialCount = 1000)
