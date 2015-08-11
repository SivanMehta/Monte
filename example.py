# import the modules we will need for our function
import math, time

# import monte carlo module
from monte import Monte


# We define the function as such because it takes a 
# minimum amount of time, regardless of computer.

# Additionally, this is a good simulation of far more convoluted functions
# which are more resource-blocking than a simple O(1) calculation
def f(x):
    time.sleep(.01)
    return math.sin(x)

# generate a list object which is passed into the tester. In this case we
# are generating a list which looks like the following:
# [-1.0, -0.999, -0.998, ..., 0.997, 0.998, 0.999]
domain = map(lambda x: x/1000.0, range(-1000, 1000))

# define the number of trials and instantiate the tester
trials = 10000
tester = Monte(f, domain, trials)

# In each of the following tests, we capture the output in the variable
# results, this is not neccessary for timing, but is just demonstrative
# in case you wanted to do some further analysis.

# run a multithreaded test
print "Multithreaded:"
start = time.time()
results = tester.test_multi()
print "\t", time.time() - start

# run a single threaded test
print "Singlethreaded:"
start = time.time()
results = tester.test()
print "\t", time.time() - start

# use result to get actual prediction for sin(0)
print sum(results)/trials
