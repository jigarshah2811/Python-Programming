"""Study: Python threading Lock, RLock, Semaphore, BoundedSemaphore,
Condition, Barrier, BoundedBarrier

https://docs.python.org/2/library/threading.html#condition-objects
"""
import collections
import threading

"""https://leetcode.com/problems/design-bounded-blocking-queue/submissions/"""


class BoundedBlockingQueue(object):
    """ Condition signals
    queue_full  and     queue_empty
    Producers get blocked in Enqueue() ---> till queue_not_full
    Consumers get blocked in Dequeue() ---> till queue_not_empty
    """

    def __init__(self, capacity: int):
        self.q = collections.deque()
        self.capacity = capacity

        # Threading and Locking thorugh Condition!
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.cond:
            # Producers get blocked in Enqueue() ---> till queue_not_full
            self.cond.wait_for(self.isNotFull)

            # Unblocked, free to produce
            self.q.append(element)

            # Notify consumers waiting on condition to unblock
            self.cond.notify()

    def dequeue(self) -> int:
        with self.cond:
            # Consumers get blocked in Dequeue() ---> till queue_not_empty
            self.cond.wait_for(self.isNotEmpty)

            # Unblocked, free to cnosume
            retval = self.q.popleft()

            # Notify Producers waiting on condition to unlock them
            self.cond.notify()

        return retval

    def size(self) -> int:
        return len(self.q)

    def isNotFull(self) -> bool:
        return len(self.q) < self.capacity

    def isNotEmpty(self) -> bool:
        return len(self.q) > 0
