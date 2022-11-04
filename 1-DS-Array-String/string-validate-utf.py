class Solution:
    def validUtf8(self, nums):
        binreps = []

        for num in nums:
            binrep = format(num, '#010b')[-8:]
            binreps.append(binrep)
        print(binreps)


        i, j = 0, 0
        while i < len(binreps):
            # Check if the string is 1-Byte, 2-Byte, 3-Byte or 4-Byte
            num1s = binreps[i].split('0')
            numBytes = len(num1s[0])
            print(numBytes)
            # Invalid scenarios
            if numBytes == 1 or numBytes > 4:
                return False

            elif numBytes == 0:
                print("hit 0-Byte!!!")
                # Valid... Continue for next
                i += 1
                continue
            else:
                # Valid... 2-Byte, 3-Byte or 4-Byte so check for next n-1 bytes are valid or not
                for j in range(i+1, i + (numBytes-1)):
                    if binreps[:2] != "10":
                        return False

            # Check next iteration
            i = j+1

        # We reach till end so everything's valid
        return True

s = Solution()
nums = [197, 130, 1]
print((s.validUtf8(nums)))
nums = [235, 140, 4]
print((s.validUtf8(nums)))
nums = [197,130,1]
print((s.validUtf8(nums)))
