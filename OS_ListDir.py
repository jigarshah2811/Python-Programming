import sys
import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath

def main(args):
    print_directory_contents(args[1])
    return 0

if __name__ == "__main__":
    main(sys.argv)
