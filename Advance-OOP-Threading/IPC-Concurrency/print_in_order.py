from threading import Thread
from threading import Barrier
from threading import Lock
from threading import Semaphore

import logging
import random
import time



class BarrierUse:
    def __init__(self):

        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self) -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        print("First ")
        self.first_barrier.wait()

    def second(self) -> None:
        self.first_barrier.wait()
        print("Second ")
        self.second_barrier.wait()

    def third(self) -> None:
        self.second_barrier.wait()
        print("Third ")


""" LOCK
Start with 2 locks, Thread1 -> Unlocks lock1 <- Thread2 waiting -> Unlocks lock2 <- Thread3 is waiting on
"""
class LockUse:
    def __init__(self):
        self.first_lock = Lock()
        self.second_lock = Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print("First ")
        self.first_lock.release()

    def second(self) -> None:
        with self.first_lock:
            print("Second ")
            self.second_lock.release()


    def third(self) -> None:
        with self.second_lock:
            print("Third ")
            self.first_lock.locked()
            self.second_lock.locked()


class SemaphoreUse:
    def __init__(self):
        self.sem = Semaphore(2)

    def first(self) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print("First ")
        self.sem.release()

    def second(self) -> None:
        with self.sem.acquire():
            print("Second ")
            self.sem.release()

    def third(self) -> None:
        with self.sem.acquire():
            print("Third ")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    """ LOCK ON THREADS !!!"""
    #obj = BarrierUse()
    obj = LockUse()
    #obj = SemaphoreUse()

    threads = set()
    doneThreads = set()

    funcs = [obj.first, obj.second, obj.third]

    for threadid in range(3):
        t = Thread(target=funcs[threadid])
        threads.add(t)

    for index, thread in enumerate(threads):
        logging.info("Main:     before joining thread %d.", index)
        thread.start()
        time.sleep(0.1)

    for index, thread in enumerate(threads):
        thread.join()
        logging.info("Main:     Thread %d joined", index)