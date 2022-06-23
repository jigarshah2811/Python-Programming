class BitArray(object):
    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = -(-numbits // 8)
        self.data = bytearray(numbytes)

    def __len__(self):
        return self.numbits

    def __setitem__(self, index, value):
        if index >= len(self):
            raise IndexError("Index is out of range")
        if not isinstance(value, int):
            raise TypeError("Value is not int type")
        if value < 0 or value > 1:
            raise ValueError("Value should be bit 0 or bit 1")
        bytenum, bitnum = divmod(index, 8)
        return (self.data[bytenum] >> bitnum) & 1   # PROBLEM

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index Out of range")
        bytenum, bitnum = divmod(index, 8)
        return (self.data[bytenum] >> bitnum) & 1

    def __repr__(self):
        if len(self) < 100:
            data = ''.join(map(str, self))  # Converting list of bits into string
        else:
            data = '...'
        return '%s(%r)' % (self.__class__.__name__, data)


def main():
    b = BitArray(20)
    print len(b)
    b[11] = 1
    b[14] = 1
    b[7] = 1
    print b

if __name__ == "__main__":
    main()
