import random
import psutil
import sys
import webbrowser
from matplotlib import pyplot as plt
from Queue import Queue
from threading import Thread


class Monte():
    def __init__(self, func, domain, trials):
        """
            domain: a list or function from which you can define the input
            function: a function that will be repeatedly run on a random value in domain
            trails: number of trials that can be run
        """
        self.func = func
        self.domain = domain
        self.trials = trials

        self.data = []

        if type(self.domain) != list or type(self.trials) != int: 
            raise TypeError

        self.q = Queue(maxsize=0)
        # generally recommended to have a max of 4 threads per core (according to by boss)
        num_threads = psutil.cpu_count() * 4

        for i in xrange(num_threads):
            worker = Thread(target = self.do_trial)
            worker.setDaemon(True)
            worker.start()
            sys.stdout.flush()
            sys.stdout.write("\rStarted %d threads... " % (i + 1))
        print "all threads started!"

    def do_trial(self):
        while True:
            x = self.q.get()

            try:
                outcome = self.func(*x)
            except TypeError:
                outcome = self.func(x)
            self.data.append(outcome)

            self.q.task_done()

    def test_multi(self):
        for i in xrange(self.trials):
            choice = random.choice(self.domain)
            self.q.put(choice)

        self.q.join()

        return self.data

    def test(self):
        outcomes = []
        for i in xrange(self.trials):
            x = random.choice(self.domain)
            try:
                outcome = self.func(*x)
            except TypeError:
                outcome = self.func(x)
            outcomes.append(outcome)

        self.data = outcomes
        return outcomes

    def plot(self):
        if len(self.data) == 0:
            raise RuntimeError("Test has not been run yet")

        plt.hist(self.data, bins = 20)
        plt.show()

    def __repr__(self):
        return "self.func: %s\nself.domain: %s\nself.trials: %d" \
        % (self.func.__name__, str(self.domain), self.trials)


def main():
    message = """
    Welcome to Monte, a multi-threaded Monte Carlo module, a web browser will now open with the documentation
    """
    print(message)
    webbrowser.open("https://github.com/SivanMehta/Monte")

if __name__ == "__main__":
    main()