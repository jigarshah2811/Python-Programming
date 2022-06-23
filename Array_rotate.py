import sys

class Solution:

    def reverseArray(self, a, start, end):
        while start < end:
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
            start+=1
            end-=1
        return a

    def rotate_array(self, a, b):
        b = b % len(a)

        a = self.reverseArray(a, 0, len(a)-1)
        print a
        a = self.reverseArray(a, 0, b-1)
        print a
        a = self.reverseArray(a, b, len(a)-1)
        return a

def main():
    array_to_rotate = [14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35]
    num_rotations = 5
    s = Solution()
    ret = s.rotate_array(array_to_rotate, num_rotations)
    print ret

if __name__ == "__main__":
    main()

