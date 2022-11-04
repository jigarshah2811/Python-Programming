import binascii

class Solution:
    def __init__(self) -> None:
        pass
    
    def processBuffer(self, buffer):

        total = len(buffer)

        start = 0
        while start < total:
            # One chunk

            # Edge case for last chunk
            if start + 16 > total:
                tmpBuffer = buffer[start: total]    # Preventing overrun on buffer
            else: 
                tmpBuffer = buffer[start: start+16]

            # PRint 3 Columns
            print(hex(start),)      # Formatting to make sure we've spaces around
            print(binascii.b2a_hex(tmpBuffer),)
            print(binascii.b2a_uu(tmpBuffer))

            start += 16     # Prepare for next iteration

buffer = b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'
s = Solution()
s.processBuffer(buffer)
