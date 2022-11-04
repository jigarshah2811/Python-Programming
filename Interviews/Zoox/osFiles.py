import subprocess
from typing import List
import os
import shutil

""" FileSystem: Example working with OS, Shell Utility and Commands """
class ExampleOSCommands:
    def readFilePaths(self, dirName: str) -> List:
        """ OS """
        files = os.listdir(dirName)         # Lists the file names within dir
        filePaths = []      

        for file in files:
            filePath = os.path.join(dirName, file)  # Joins two path (dir, fileName)
            filePaths.append(filePath)
        
        """ Shell utiliy """
        for filePath in filePaths:
            shutil.chown(filePath, "jshah")     # Change permissions of a file on filesystem
            fileName = filePath.split("/")[-1]  # Last name is file name in path Example: ./Square/Design_SnakeGame.py
            destPath = shutil.copy(filePath, os.path.join("../Zoox", fileName))     # COPY file from src to dest
            print(f"copied from {filePath} to {destPath}")

        """ Commands """
        for filePath in filePaths:
            fileName = filePath.split(".")[-1]
            print(f"listing {fileName}")
            echoCmd = subprocess.run(   ['ls', '-l', fileName],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True)
            stdout, stderr = echoCmd.stdout, echoCmd.stderr
            print(stdout, stderr)

s = ExampleOSCommands()
dirName = "../Square"
s.readFilePaths(dirName)
