"""
# A spaceship is approaching some planets that are arranged in a 1-dimensional line. It needs to pass through the line of the planets, but can't get too close to any planet, otherwise it would get caught in that 
# planet's gravitational field.
# Given a list of planets, where each planet is specified by its position along the line and the range of its gravitational field, compute the list of gaps from [0, 1000] through which the spaceship can fly.    
# input                output (gaps)           reasoning
# [location, orbit]       
# [3,2]                [0,1],[5,1000]       The field covers [1,5].
# [3,2],[5,1]          [0,1],[6,1000]          The fields cover [1,5] and [4,6].
# [2,1],[5,1]          [0,1],[3,4],[6,1000]    The fields cover [1,3] and [4,6].
# [2,2],[7,1],[4,1]    [5,6],[8,1000]          The fields cover [0,4], [6,8], and [3,5].



# [4,1] [5,3] --->.  sort by LOCATION OR Sort by orbit 
# [3, 5] [2, 8] 
#    For every input
#         CALC RANGE
#     range-             range+
#    1<--------- LOCATION --------->5
   

# SORT FIELDCOVERS ==== SORT By Location   
#    # The fields cover [1,5] and [4,6].
#    GAP [0, 1000]. [0 3] [5-8], [10-1000]
   
#    sort by START of RANGE   ===> O(NLogN)
#    for coverrange in coverRANGEs:
        
#       reducedGap = Exclude coverragnge
#       [0,1] and [5 1000]
      
  
"""

class Solution:
    def __init__(self):
        pass
    
    def findGravity(self, inputs): # inputs = [[3, 2], [5, 1]]
        fieldCovers = []
        for input in inputs:
            location, orbit = input[0], input[1] # [3, 2]
            
            fieldCovers.append([location-orbit, location+orbit])            
        
        
        
        # Exclude field cover from [0, 1000] gap
       
        res = [[0, 1000]]
        # SORT
        fieldCovers = sorted(fieldCovers, key= lambda x: x[0])
        # [[1, 5], [4, 6]]
        print(fieldCovers) # FieldCovers = [[1, 5], [4, 6]]
        for fieldCover in fieldCovers:
            # The fields cover [1,5] and [4,6]
            start, end = fieldCover[0], fieldCover[1]
            # start: 1, end: 5
            
            # [0, 1000]
            # [0, 1] [5,1000] -> incorporate [4,6]
            # [6, 1000]
            prev = res[-1]
            if start <= prev[0]:
                prev[0] = end       # Update START of last result to exclude this fieldCover
            else:
                prev[1] = start     # Update END of last result to exclude this fieldCover [0, 1000]: [2, 4]: [0, 2] and [4: 1000]
                res.append([end, 1000])
    
        return res
            
            # [3, 1000] ->[4,6] = [3, 4] [6,1000]

            # [0, 1][6, 1000]
        
            
    
s = Solution()
inputs = [[3, 2], [5, 1]]
print(s.findGravity(inputs))
inputs = [[2,2],[7,1],[4,1]]
print(s.findGravity(inputs))

"""
    # [3,2]             [0,1],[5,1000]       The field covers [1,5].
# [3,2],[5,1]          [0,1],[6,1000]          The fields cover [1,5] and [4,6].
# [2,1],[5,1]          [0,1],[3,4],[6,1000]    The fields cover [1,3] and [4,6].
# [2,2],[7,1],[4,1]    [5,6],[8,1000]          The fields cover [0,4], [6,8], and [3,5].

"""