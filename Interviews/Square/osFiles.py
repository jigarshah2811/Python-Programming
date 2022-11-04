import subprocess
from typing import List
import os
import shutil

""" FileSystem: Example working with OS, Shell Utility and Commands """
class ExampleOSCommands:
    def readFilePaths(self, dirName: str) -> List:
        """ OS """
        print(f"\n########## OS Example: list dirs and join filePaths ##########")
        files = os.listdir(dirName)         # Lists the file names within dir
        filePaths, fileNames = [], []

        for file in files:
            filePath = os.path.join(dirName, file)  # Joins two path (dir, fileName)
            filePaths.append(filePath)
            fileName = filePath.split("/")[-1]  # Last name is file name in path Example: ./Square/Design_SnakeGame.py
            fileNames.append(fileName)
        
        """ Shell utiliy """
        print(f"\n###### Shell Utility Example: Copying file from src to dest ########")
        for filePath in filePaths:
            shutil.chown(filePath, "jshah")     # Change permissions of a file on filesystem            
            destPath = shutil.copy(filePath, os.path.join("../Zoox", fileName))     # COPY file from src to dest
            print(f"copied from {filePath} to {destPath}")

        """ Commands: Subprocess module """
        print(f"\n###### SubProcess Module Example: Running command ls -l <fileName> #######")
        for fileName in fileNames:
            echoCmd = subprocess.run(   ['ls', '-l', fileName],     # Running a command "ls -l <fileName>"
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True)    # This is for decoded version of stdout and stderr
            stdout, stderr = echoCmd.stdout, echoCmd.stderr
            print(stdout, stderr)

s = ExampleOSCommands()
dirName = "../Square"
s.readFilePaths(dirName)
