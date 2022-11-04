
""" Q: Find speedy dianosors

You will be supplied with two data files in CSV format. The first file contains
statistics about various dinosaurs. The second file contains additional data.
Given the following formula,

speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (acceleration due to gravity on earth)

Write a program to read in the data files from disk, it must then print the
names of only the bipedal dinosaurs from fastest to slowest. Do not print any
other information.

=== Input data files ===

$ cat dinosours1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat dinosours1.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
"""


import collections
import math
class Solution:

    def __init__(self):
        self.d = collections.defaultdict(list)          # {NAME: [LEGLEN, STRIDELEN]}
        self.speed = collections.defaultdict(float)     # {NAME: CalculatedSPEED}

    def calcSpeed(self, file1, file2):
        with open(file1) as f1:
            lines = f1.readlines()
            for line in lines:
                (name, legLen, _) = line.split(",")
                self.d[name].append(float(legLen))
                # REVISIT if anything else is needed for SPEED

        with open(file2) as f2:
            lines = f2.readlines()
            for line in lines:
                (name, strideLen, stance) = line.split(",")
                self.d[name].append(float(strideLen))
                self.d[name].append(stance.rstrip())
                # REVISIT if anything else is needed for SPEED        


        print(f".....After reading files...")   # # {NAME: [LEGLEN, STRIDELEN, STANCE]}
        for name, l in self.d.items():
            print(name, l)



        # Calc speed
        for name, l in self.d.items():
            if len(l) > 2:      # {NAME: [LEGLEN, STRIDELEN, STANCE]}
                LEG_LENGTH, STRIDE_LENGTH, STANCE = l[0], l[1], l[2]

                # calc Speed
                G = 9.8     # (acceleration due to gravity on earth)
                speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * G)

                self.speed[name] = speed
        print(f"......After calc speed")
        for name, speed in self.speed.items():
            print(name, speed)

         # DICTIONARY: SORT BY VALUES!!!
        speedyNames = sorted(self.speed, key=self.speed.get, reverse=True)        # Dinosors with SPEED: # {NAME: CalculatedSPEED}
        return speedyNames


s = Solution()
print(s.calcSpeed("dinosours1.csv", "dinosours2.csv"))