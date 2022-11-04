"""
Given input like:

View events:
photoId | photographerId | viewerUserId | timestamp
--------+----------------+--------------+-----------
photo1  | photographer1  | user1        | 1
photo1  | photographer1  | user2        | 2 # THIS MATTERS, LAst Event before the FOLLOW Event timestamp
photo2  | photographer1  | user1        | 3
photo1  | photographer1  | user1        | 6 # NONOOOP


Follow events:

photographerId | viewerUserId | timestamp
---------------+--------------+-----------
photographer1  | user1        | 4


Expected output would be:

photoId | views | follows
--------+-------+---------
photo1  | 2     | 0        <- photo1 was viewed twice, but no "follow" attributions
photo2  | 1     | 1        <- photo2 was viewed once, and gets the attribution for the follow event


# VIEW COUNT -- FREQ MAP { PhotoID: CountOfViews }

# FOLLOWS count --- What was the MOST recent views 
                    KEY
ORDERED MAP VIEWMAP ---   { user: TimeStamp }               ===> Result { PhotoID: countFollow (users)}



For each FollowEvent:
    Look for TimeStamp, User


MAxHEAP ---   (timestamp, userID, photoID) ----- MaxHeap per User, MaxHeap per Photo.... 

"""
from collections import defaultdict, OrderedDict
import unittest

class Solution:
    def __init__(self, viewEvents, followEvents): 
        self.viewEvents = viewEvents
        self.followEvents = followEvents

        self.freqMap = defaultdict(int)  # VIEW COUNT -- FREQ MAP { PhotoID: CountOfViews }
        self.viewsMap = OrderedDict()    # ORDERED MAP VIEWMAP ---   { user: TimeStamp }               ===> Result { PhotoID: countFollow (users}
        self.res = defaultdict(list)    # {userid: [views, follows]}
    
        self.buildfreqMaps()
        self.buildviewsMap()
        
    def buildfreqMaps(self):
        """
        viewEvents = [
            ["photo1", "user1", 1],
            ["photo1", "user2", 2],
            ["photo2", "user1", 3],            
            ["photo3", "user1", 6],
        ]
        """
        for viewEvent in self.viewEvents:
            (photoID, user, timestamp) = viewEvent[0], viewEvent[1], viewEvent[2]
            self.freqMap[photoID] += 1  # assuming unique view per timestamp
            
    
    def buildviewsMap(self):
        """            
        followEvents = [
            ["user1", 4]
        ]
        """
        for followEvent in self.followEvents:
            (user, timestamp) = followEvent[0], followEvent[1]
            self.viewsMap[user] = timestamp
        
    
    def figureViews(self):
        # Building OUTPUT:         self.res = defaultdict(list)    # {photoID: [views, follows]}
        for photoID, freq in self.freqMap.items():
            self.res[photoID].append(freq)
        
        return self.res
    
    def figureFollows(self):
        for followEvent in self.followEvents:
            (user, timestamp) = followEvent[0], followEvent[1]
            
            # Look at the last entries per timestamp order
            for viewedUser, viewedtimestamp in reversed(self.viewsMap.items()):    # Looking backwards in OrderedDict arranged by Timestamp
                # ORDERED MAP VIEWMAP ---   { user: TimeStamp }
                if viewedUser != user:  # skip other user's entries
                    continue

                if viewedtimestamp >timestamp:      
                    continue    # Skip entries AFTER timestamp (Future)
                
                # Building output
                # self.res = defaultdict(list)    # {userid: [views, follows]}
                self.res[user].append(viewedtimestamp)   # Bingo: Most RECENT Timestamp ENTRY
                break
            
        return self.res
                
            
        
"""
class TestSolution(unittest.TestCase):
    def __init__(self) -> None:
        super().__init__()
        

    def testBuildFreqMap(self):
        viewEvents = [
            ["photo1", "user1", 1],
            ["photo1", "user2", 2],
            ["photo2", "user1", 3],            
            ["photo3", "user1", 6],
        ]
        followEvents = [
            ["user1", 4]
        ]
        s = Solution(viewEvents, followEvents)

        s.buildfreqMaps(viewEvents)
        
        self.assertNotEqual(s.freqMap, None)

    def testBuildViewsMap(self):
        
        
    def testFigureViews(self):
    def testFigureFollows(self):
"""
    
def main():
    viewEvents = [
        ["photo1", "user1", 1],
        ["photo1", "user2", 2],
        ["photo2", "user1", 3],            
        ["photo3", "user1", 6],
    ]
    
    followEvents = [
        ["user1", 4]
    ]
    s = Solution(viewEvents, followEvents)
    print(s.figureViews())
    print(s.figureFollows())
    
    # Run tets
    
    
if __name__ == "__main__":
    main()