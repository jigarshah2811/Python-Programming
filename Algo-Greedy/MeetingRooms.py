"""
Algorithm: GREEDY       DS: MIN-HEAP (To maintain meeting end-times)
Make sure the intervals are in sorted order before processing, In this case, sort by "start time"

Case 1: START of this meeting is > end of shortest meeting --- Need new meeting room
Case 2: START of this meeting is < end of shortest meeting --- Re-use same meeting room ---> update end 

"""
import heapq
class Solution:
    def minMeetingRooms(self, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0]) # Sort meetings by start time
        
        
        # Heap of [meeting[END_TIME]] 
        # Example: intervals = [[0,30],[5,10],[15,20]] rooms: [10, 20, 30] 
        rooms = []      
        
        
        START_TIME, END_TIME = 0, 1
        for i, meeting in enumerate(meetings):
            if i == 0:  # 1st meeting --- Need new meeting room
                heapq.heappush(rooms, meeting[END_TIME])
                continue
            
            # print(f"rooms: {rooms}, meeting: {meeting}")
            
            # Case 2: START of this meeting is < end of shortest meeting --- Re-use same meeting room ---> update end            
            lastMeetingEnding = rooms[0]
            if meeting[START_TIME] >= lastMeetingEnding:
                heapq.heapreplace(rooms, meeting[END_TIME])
            
            # Case 1: START of this meeting is > end of shortest meeting --- Need new meeting room
            else:
                heapq.heappush(rooms, meeting[END_TIME])
        
        return len(rooms)
                