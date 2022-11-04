"""  https://leetcode.com/problems/encode-and-decode-strings/submissions/
"""
from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Pattern: encodedStr: 5/Hello11/HelloWorld           len(s)/ActualString
        """
        
        encodedStr = ""
        for s in strs:
            """ encodedStr: 5/Hello """
            encodedStr += f"{len(s)}" + "/"
            encodedStr += s
        
        print(f"Encoded: {encodedStr}")
        return encodedStr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        start, end = 0, 0
        while end < len(s):
            if s[end] == "/":      # Seperator, Hisab for len(s) + "/" + actualString
                lenStr = int(s[start:end])              # len in int
                                                        # skip "/"
                decodedStr = s[end+1 : end+1+lenStr]    # actualString 
                print(f"deocdedStr: {decodedStr}")
                
                res.append(decodedStr)
                
                
                # Prepare for next str
                end = end + 1 + lenStr                  # should be at next string's LEN
                start = end
                
            else:   # Normal char
                end += 1
        
        return res
                
        
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ["Hello","World"]
print(codec.decode(codec.encode(strs)))     # output: ["Hello","World"]
