N = 3
import collections


class Solution(object):
    def __init__(self):
        self.q = collections.deque()
        # Queue((Second, Frequency), )

    def eventOccured():
        timeMS = getEpochInMill()

        second = qtimeMS // 1000

        (s, c) = q[-1]
        if s == second:
            q[-1][1] += 1  # HERE we can save MAX

            # if max(q[-1][1], maxval)

        else:
            q.append((second, 1))

        # Purge old records
        while len(e) > N:
            q.popleft()

    def getNumEvents():
        res = 0

        # Purge old records
        while len(self.q) > N:
            q.popleft()

        for ele in self.q:
            res += ele[1]

        return res


s = Solution()

assert (s.getNumEvents() == 0)

for i in range(5):
    s.eventOccured()
    time.sleep(1000)  # Adding 5 events in 5 seconds

assert (s.getNumEvents() == 5)

for i in range(5):
    s.eventOccured()
    time.sleep(10)  # Adding 5 events in 6th second

assert (s.getNumEvents == 7)
