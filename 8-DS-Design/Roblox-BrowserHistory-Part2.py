"""
Support for multiple tabs: Now we want to support 1...n at the same time, with history tracked separately in all. You may modify existing methods to support this expanded behavior.
 
Functionality to be added:
- open a new tab
- close an existing tab
 
 
other methods as you see fit
"""
import collections


class Browser:
    def __init__(self, homepage):
        # List of BrowserHistory
        self.mapTabToHistory = collections.defaultdict(BrowserHistory)
        
        # {"Name": object of BrowserHistory}
        
    def openTab(self, name, homepage):
        self.browserHistoryTab = BrowserHistory(homepage)
        self.mapTabToHistory[name] = self.browserHistoryTab

        
    def getHistory(self, name):
        return self.mapTabToHistory[name]
        
    def closeTab(self, name):
        del  self.mapTabToHistory[name]

obj = Browser()
obj.openTab("1", "roblox.com")
obj.openTab("2", "leetcode.com")
obj.openTab("3", "codesignal.com")

obj.getHistory("1").visit("facebook.com")
obj.getHistory("1").back(5)

obj.openTab("2").visit("google.com")
obj.openTab("2").back(5)

""""
PART 3: Make it THREAD SAFE 
Use locks for atomic operations on browserHistory
"""
# n = 0
# lock = threading.Lock()

# def foo():
#     global n
#     with lock:
#         n += 1