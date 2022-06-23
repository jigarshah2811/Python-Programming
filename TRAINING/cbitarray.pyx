'Goal:  Build a new bitarray class modeled after bytearray which was itself modeled after lists'

class BitArray:
    'Space-efficient bit array built on top of byte arrays'

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = -(-numbits // 8)                        # ceiling division
        self.data = bytearray(numbytes)

    def __len__(self):
        return self.numbits

    def __getitem__(self, int index):
        cdef int bytenum, bitnum
       
        if index >= len(self):
            raise IndexError
        bytenum = index >> 3
        bitnum = index & 7
        return (self.data[bytenum] >> bitnum) & 1

    def __setitem__(self, index, value):
        if index >= len(self):
            raise IndexError
        if not isinstance(value, int):
            raise TypeError('A integer bit 0 or 1 is required')
        if value < 0 or value > 1:
            raise ValueError('A integer bit 0 or 1 is required')
        bytenum, bitnum = divmod(index, 8)
        mask = 1 << bitnum
        if value:        
            self.data[bytenum] |= mask
        else:
            self.data[bytenum] &= ~mask

    def __repr__(self):
        if len(self) < 100:
            data = ''.join(map(str, self))
        else:
            data = '...'
        return '%s(%r)' % (self.__class__.__name__, data)
                           

if __name__ == '__main__':
    b = BitArray(20)
    print len(b)
    b[11] = 1
    b[14] = 1
    b[7] = 1
    b[11] = 0
    print list(b)
