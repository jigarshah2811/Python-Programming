"""
https://leetcode.com/problems/sender-with-largest-word-count/
"""

from collections import defaultdict
from typing import List
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # Build FreqMap
        freqMap = defaultdict(int)
        maxTimes = 0
        
        for s, m in zip(senders, messages):
            words = len(m.split(" "))
            freqMap[s] += words
            
            # keep track of max number of words spoken by any sender
            maxTimes = max(maxTimes, freqMap[s])
        
        # Senders should be in sorted order!
        targetSender = ''
        for s, times in freqMap.items():
            if times == maxTimes:
                # If this sender spoke max words, We found the target Sender!
                # BUT if multiple senders, sender should be in lexographic sorted order
                if targetSender < s:
                    targetSender = s
        
        
        return targetSender
                