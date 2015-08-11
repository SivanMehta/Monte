import webbrowser

import random
import psutil
from Queue import Queue
from threading import Thread




def main():
    message = """
    Welcome to Monte, a multithreaded Monte Carlo module, a web browser will now open with the documentation
    """
    print(message)
    # webbrowser.open("https://www.facebook.com/")

if __name__ == "__main__":
    main()