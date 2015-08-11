import webbrowser

from matplotlib import pyplot as plt
import random
import psutil
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

        self.data = None

        if type(self.domain) != list or type(self.trials) != int: 
            raise TypeError

    def test(self):
        outcomes = []
        for i in xrange(self.trials):
            x = random.choice(self.domain)
            outcome = self.func(x)
            outcomes.append(outcome)

        self.data = outcomes
        return outcomes

    def plot(self):
        if self.data == None:
            raise RuntimeError("Test has not been run yet")

        plt.hist(self.data, bins = 20)
        plt.show()

    def __repr__(self):
        return "self.func: %s\nself.domain: %s\nself.trails: %d" \
        % (self.func.__name__, str(self.domain), self.trials)


def main():
    message = """
    Welcome to Monte, a multithreaded Monte Carlo module, a web browser will now open with the documentation
    """
    print(message)
    webbrowser.open("https://www.facebook.com/")

if __name__ == "__main__":
    main()