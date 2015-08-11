import webbrowser

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

        if type(self.domain) == type(lambda x: x):
            raise TypeError("Testing with function is not yet implemented")

    def test(self):
        pass

    def __repr__(self):
        return "self.func: %s\nself.domain: %s\nself.trails: %d" \
        % (self.func.__name__, str(self.domain), self.trials)


def main():
    message = """
    Welcome to Monte, a multithreaded Monte Carlo module, a web browser will now open with the documentation
    """
    print(message)
    # webbrowser.open("https://www.facebook.com/")

if __name__ == "__main__":
    main()