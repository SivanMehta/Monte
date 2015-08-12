# Multithreaded Monte Carlo Testing

A [Monte Carlo Simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method) is a simple way of testing a hypothesis. In alignment with the intrinsic nature of the simulation, you should be able to run each trials in parallel, given their statistically independent nature. This lends itself to using the `threading` module in Python. 

Currently, the module contains a class, simply called `Monte`. You can use this as a simple way of testing outcomes.

### Usage

Here is a simulation attempting to guess the average value of `math.sin` for the range (-1, 1). You can see a fully fleshed out version of this in `example.py`. First, you have to import the modules you're going to use and define the function you are going to test. Here, we will be simulating a function that takes .01 seconds to run

```python
import math, time
from monte import Monte

def f(x):
    time.sleep(.01)
    return math.sin(x)
```

Next, we must define the domain over which we are testing. Ideally, we would just provide a function, but that has yet to be implemented. Instead, simply provide a `list` object. Here, we are using the numbers -1 to 1 with increments of .001.

```
domain = map(lambda x: x/1000.0, range(-1000, 1000))
# produces [-1.0, -0.999, -0.998 ... 0.997, 0.998, 0.999]
```
Next, define the number of trials you are going to do, and create the tester!

```
trials = 10000
tester = Monte(f, domain, trials)
```

After generating the tester, you can run either a single-threaded or multi-threaded test. You can see the remarkable gains when demonstrated here:

```python
tester = Monte(f, a, trials)

# multi-threaded
results = tester.test_multi()

# single-threaded
results = tester.test()

```
which gives the following results:

```bash
$ python example.py
Started 16 threads... all threads started!
Multithreaded:
	8.11027097702
Singlethreaded:
	118.53207612
```
Clearly, the multithreaded version is significantly faster for testing this function.
