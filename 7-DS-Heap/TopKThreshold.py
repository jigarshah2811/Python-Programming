#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#
import collections
import heapq

def processLogs(logs, threshold):
    # Counting TXNs per user
    d = collections.defaultdict(int)
    for record in logs:
        entry = record.split(" ")
        fromUser, toUser, amount = entry[0], entry[1], entry[2]
        if fromUser == toUser:  # Same user transacting
            d[fromUser] += 1
        else:                   # diff users
            d[fromUser] += 1
            d[toUser] += 1
    
    print(d)
    
    # SORTING
    h = []
    for user, numTxn in d.items():
        if numTxn >= threshold:
            heapq.heappush(h, (numTxn, user))
    print(h)
    
    # Results in Ascending order of numTxn
    res = []
    
    while h:
        (numTxn, user) = heapq.heappop(h)
        res.append(user)
    
        
    return res

logs = [
    1 2 50
    1 7 70
    1 3 20
    2 2 17
]
processLogs()