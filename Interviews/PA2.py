

# Your previous Plain Text content is preserved below:

# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!


"""
Given an array of integers greater than zero, find if there is a way to
split the array in two (without reordering any elements) such that the
numbers before the split add up to the numbers after the split. If so,
print the two resulting arrays.

=== Test cases ===

In [1]: can_partition([5, 2, 3]) 
Output [1]: ([5], [2, 3]) 
Return [1]: True 
 
In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1]) 
Output [2]([2, 3, 2], [1, 1, 1, 2, 1, 1]) 
Return [2]: True 

In [3]: can_partition([1, 1, 3]) 
Return [3]: False 

In [4]: can_partition([1, 1, 3, 1]) 
Return [4]: False
""" 

class Solution:
    def can_partition(nums):
        LSum, RSum = 0, sum(nums)
        for i, num in enumerate(nums):
            L = nums[:i]    # <--- ..i-1
            R = nums[i:]    # ---->    i...
            Lsum += num
            Rsum -= num

            if Lsum == Rsum:
                return(L, R)
        
        return None

s = Solution()

nums = [5, 2, 3]
print(s.can_partition(nums))    # output Output [1]: ([5], [2, 3]) 


"""
You will be supplied with two data files in CSV format. The first file contains
statistics about various dinosaurs. The second file contains additional data.
Given the following formula,

speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (acceleration due to gravity on earth)

Write a program to read in the data files from disk, it must then print the
names of only the bipedal dinosaurs from fastest to slowest. Do not print any
other information.

=== Input data files ===

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
"""
# m {NAME: SPEED}
# SORT BY VALUES  ----> FASTEST TO SLOWEST ---> Print in Reverse

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
                (name, legLen, diet) = line.split(",")
                self.d[name].append(legLen)
                # REVISIT if anything else is needed for SPEED

        with open(file2) as f2:
            lines = f2.readlines()
            for line in lines:
                (name, strideLen, diet) = line.split(",")
                self.d[name].append(strideLen)
                # REVISIT if anything else is needed for SPEED        


        print(f"After reading files: {self.d}")   # # {NAME: [LEGLEN, STRIDELEN]}



        # Calc speed
        for name, l in self.d.items():
            if len(l) == 2:
                LEG_LENGTH, STRIDE_LENGTH = l[0], l[1]
                G = 9.8     # (acceleration due to gravity on earth)

                speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * G)

                self.speed[name] = speed

        # Dinosors with SPEED: # {NAME: CalculatedSPEED}
        speedyNames = sorted(self.speed, key=lambda x: x[0], reversed=True)

        res = []
        for name, speed in speedyNames.items():
            res.append(name)

        return res


