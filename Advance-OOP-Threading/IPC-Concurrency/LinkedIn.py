"""
public class HelloWorld {

  public static void main(String[] args){
    //Prints "Hello, World" to the terminal
    System.out.println("Hello, World");
  }

}
dfdsafds
HERE

// Let's implement two methods hydrogen()  () and oxygen(). Different threads will run these methods and when 2 H and 1 O threads come together we make molecule (print something.. ) keep going throug remaining Hydrogen and Oxygen atoms.

"""
"""
2 Methods... Semaphores and ConditionVariables
H20


HHHO
OH
"""


class Solution:
    def __init__(self):
        self.hSem = Semaphore(2)  # 2 to 1 to 0
        self.oSem = Semaphore(1)  # 1 to 0
        self.h2oLock = Lock()

        self.hCount
        self.oCount

    def hydrogen():
        self.hSem.acquire()

        # Work    # giving Hydrozen
        doWork()  # INcrease hCount
        self.h2oLock.acquire()
        self.hCount += 1
        self.h2oLock.release()

        self.hSem.release()

    def oxygen():
        self.oSem.acquire()

        #    Execute    # giving oxy
        doWork()  # Increase oCount

        self.h2oLock.acquire()
        self.oCount += 1
        self.h2oLock.release()

        # Wait for 2 Hydrozen to complete
        self.oSem.release()

    def formsH2O():
        if hCount >= 2 and oCount >= 1:  # Have enought form
            self.h2oLock.acquire()

            hCount -= 1
            oCount -= 1

            self.h2oLock.release()
            numH2O += 1


class Solution:
    def __init__(self):

        self.h2oLock = Lock()

        self.cond = Condition()

    def hydrogen():

        # Work    # giving Hydrozen
        doWork()  # INcrease hCount
        self.h2oLock.acquire()
        self.hCount += 1
        self.h2oLock.release()

        with self.cond:
            self.cond.waitfor(check)
            formsH2O()

    def oxygen():

        # self.oSem.acquire()

        #    Execute    # giving oxy
        doWork()  # Increase oCount

        self.h2oLock.acquire()
        self.oCount += 1
        self.h2oLock.release()

        with self.cond:
            self.cond.waitfor(check)
            formsH2O()

        # Wait for 2 Hydrozen to complete
        # self.oSem.release()

    def check():
        return hCount >= 2 and oCount >= 1

    def formsH2O():
        if hCount >= 2 and oCount >= 1:  # Have enought form
            self.h2oLock.acquire()

            hCount -= 1
            oCount -= 1

            self.h2oLock.release()
            numH2O += 1

            LOCKLESS
            QUEUE == == FAST

            HHHHHHHH

            HHHHHH
            len(hq) > 2

            00000
            len(oq) > 1

            00000000000000000
            HHHHHHHHH0

            Producer
            Queue
            Consumer
            Queue

            class Solution:

    def __init__(self):
        self.cond = Condition()

    def hydrogen():
        with self.cond:
            h += 1

            self.cond.waitfor(check)

            if h > 2:
                hCond.set()

            cond.notifyall()

    def oxygen():

        with self.cond:
            o += 1

            self.cond.waitfor(check)

            if o > 1:
                oCond.set()

            cond.notifyall

    def formsH2O():
        if hCount >= 2 and oCount >= 1:  # Have enought form
            self.h2oLock.acquire()

            hCount -= 1
            oCount -= 1

            self.h2oLock.release()
            numH2O += 1
