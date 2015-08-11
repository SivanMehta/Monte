import math, time
from monte import Monte

def f(x):
    time.sleep(.01)
    return math.sin(x)

domain = range(-1000, 1000)
domain = map(lambda x: x/1000.0, a)
# [-1.0, -0.999, -0.998, -0.997, -0.996 ...
# 0.995, 0.996, 0.997, 0.998, 0.999]
trials = 10000

tester = Monte(f, a, trials)

print "Multithreaded:"
start = time.time()
results = tester.test_multi()
print "\t", time.time() - start


print "Singlethreaded:"
start = time.time()
results = tester.test()
print "\t", time.time() - start