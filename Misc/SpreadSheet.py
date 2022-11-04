import pprint
from textwrap import indent
class SpreadSheet(object):
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.items = [["" for col in range(self.cols)] for row in range(self.rows)]
        self.maxColLen = 0

    def __update__(self, row, col, val):
        self.maxColLen = max(self.maxColLen, len(str(val)))  # Update max column length to be the largest string item to fit
        self.items[row][col] = val

    def __print__(self):
        print("Printing items...")
        for row in range(self.rows):
            printRow = ""
            for col in range(self.cols):
                if self.items[row][col]:
                    printCol = "{0}".format(self.items[row][col])
                    if col < self.cols-1:
                        printCol = printCol + "|"
                    printRow += printCol
            print(printRow)
        print("")


    def __prettyPrint__(self):
        print("Pretty Print...")
        custom_printer = pprint.PrettyPrinter(indent=4, width=100)
        for row in range(self.rows):
            custom_printer.pprint(self.items[row])


rows, cols = 4, 3
s = SpreadSheet(rows, cols)
s.__update__(0, 0, "bob")
s.__update__(0, 1, 10)
s.__update__(0, 2, "foo")

s.__update__(1, 0, "alice")
s.__update__(1, 1, 5)

s.__print__()
s.__prettyPrint__()