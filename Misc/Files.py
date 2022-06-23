import os
with open("filesToRemove") as f:
    lines = f.readlines()
    for line in lines:
        line = "{}".format(line)
        print(line)
        os.remove(line)


