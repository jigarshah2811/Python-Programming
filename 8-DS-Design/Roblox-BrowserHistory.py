"""
Write a simple browser history functionality for a single tab browser.
The default webpage for every tab is "roblox.com".
Allow for visiting any webpage, and browsing back and forward with variable depth.
Your code should have the following public methods, but feel free to add any other methods
or functions that can help you debug or check your solution.
 
 Q1  
 robox ---> google --->
 Q2
 AFter (back-1) and visit(fb)
            cur
 roblox --> fb      CLEARS FORWARD HISTORY (TAKE THIS CLUE WHILE CODING)
 
 
 Q3.        CUR (back <-- 5)
 roblox --> fb      CLEARS FORWARD HISTORY (TAKE THIS CLUE WHILE CODING)
 
 Not going to RENDER a page
 
 Array.     visit: add a new URL entry in tail ------- IF cur == tail or cur in middle .... get rid of everything after middle
            back: moving pts (cur - steps)  protect boundaries
            fwd: moving pts (cur+steps)
 [  homepage, ]
          cur
 [roblox, google, fb, somethingelse]
 
 visits(codesignal)
 
 Optimized approach:       cur
 stackHistory = [homepage, url1]   --- My cur is always going  
 stackForward = [url2, url3]
 
void visit(string destinationUrl)
 - goes to a given URL
 - starts new forward history
 
string back(int steps)
 - goes back in browsing history by the number of steps
 - returns the URL at that point in history
 
string forward(int steps)
 - goes forward in history by the number of steps
 - returns the URL at that point in history
 - note: user can only go forward after coming back in history first

"""

class BrowserHistory:
    def __init__(self, homepage):
        self.stack = [homepage]     # Stack: [a]
        self.fwdStack = []
    
    
    def visit(self, url):
        self.stack.append(url)      # stack: [a,b]
        # CLEARS FORWARD HISTORY (TAKE THIS CLUE WHILE CODING)
        self.fwdStack = []          # stack=[a] fwdStack=[b]
        
                                    # stack=[a, d]  fwdStack=[]
        
    def back(self, steps):  # back(2)
        # OOB? 
        steps = min(steps, len(self.stack)-1)   # steps:1
        
        # Make sure leave 1 items in stack
        for i in range(steps):
            url = self.stack.pop()          
            self.fwdStack.append(url)       
                                            # stack=[a] fwdStack=[b]
        
        return self.stack[-1]       # return 'a'
        
    def forward(self, steps):
                                       # stack=[a, d]  fwdStack=[]
        for i in range(steps):
            if not self.fwdStack:
                break    
            else:
                url = self.fwdStack.pop()
                self.stack.append(url)
            
        return self.stack[-1]            # return 'd'
        
    def printHistory(self):
        print(self.stack)
        print(self.fwdStack)
    
#  homepage = a
#  visit(b) ... visit(c) -> user should see 'c'
#  back(2) -> user should see 'a'
#  visit(d) -> user should see 'd' (history is [a,b,c,d])
# forward(2)

"""" WRITING TESTS """""""""
# Unittests
# import unittests

# class TestBrowserHistory:
#     def testVisit
#     def testBack
#     def testForward

browserHistory = BrowserHistory("roblox")
print(browserHistory.visit("google"))
print(browserHistory.printHistory())    # ['roblox', 'google']

print(browserHistory.visit("fb"))
print(browserHistory.printHistory())    # ['roblox', 'google', 'fb']

print(browserHistory.back(2))  # return robox
print(browserHistory.printHistory())    # roblox


print(browserHistory.forward(2))  # return 
print(browserHistory.printHistory())    # 

"""
print(browserHistory.visit("codesignal"))    # 
print(browserHistory.printHistory())

print(browserHistory.forward(1))   # return codesignal
print(browserHistory.printHistory())
print(browserHistory.visit("codesignal2"))
print(browserHistory.printHistory())

assert(browserHistory.back(1) == "codesignal")
"""

""" Using Single List """
class BrowserHistoryOptimized:
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0                # keeps track of cur homepage, after back//forward 
    
    def visit(self, url):
        self.history = self.history[0:self.cur+1] # DISCARD FORWARD HISTORY 
        
        self.history.append(url)
        self.cur = len(self.history)-1
        
    def back(self, steps):
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
    
    def forward(self, steps):
        self.cur = min(self.cur + steps, len(self.history)-1)
        return self.history[self.cur]
    
    

""" Using 2 stacks .... history=[url1, url2, url3] homepage is always last
                        forward=[url4, url5, ...]
                        back(steps)     pulls from history and pushes in forward ---->
                        forward(steps)  pulls from forward and pushes back in history <-----
 """
class BrowserHistoryLeetCode:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.forwardStack = []
        
        
    def visit(self, url: str) -> None:
        self.stack.append(url)      # Add new URL on top of stack == HOMEPAGE
        self.forwardStack = []      # visiting new URL, invalidates all forwardURLs
        print(f"stack after visit: {self.stack}, forwardStack: {self.forwardStack}")
        

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.stack)-1)
        for i in range(steps):
            self.forwardStack.append(self.stack.pop())
        
        print(f"stack after back: {self.stack}, forwardStack: {self.forwardStack}")
        return self.stack[-1]   # HOMEPAGE changed to back(steps) URL

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.forwardStack:
                break
            else:
                self.stack.append(self.forwardStack.pop())
        
        
        print(f"stack after forward: {self.stack}, forwardStack: {self.forwardStack}")
        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)