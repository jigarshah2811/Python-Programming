import sys
import os


def printList(path):
    try:
        contentlist = os.listdir(path)
    except ValueError:
        print "Invalid path " % path % " Try again....."
        return

    for content in contentlist:
        subDir = os.path.join(path, content)
        if os.path.isdir(subDir):
            printList(subDir)
        else:
            print content


def main(args):
    printList(args[1])

if __name__ == "__main__":
    main(sys.argv)
