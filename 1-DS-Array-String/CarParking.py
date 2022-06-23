class Solution:
    def parkingCars(self, parking):
        freeSlot = len(parking)-1

        for i, car in enumerate(parking):
            if car == i:    # If Car#K is already at ParkingSlot#K then no movement required
                continue
            
            # For car#i find target slot#i
            targetSlot = car
            if parking[targetSlot] != -1:   # If target slot is NOT available, 
                # make it available by moving the car from targetSlot to freeSlot
                parking[targetSlot], parking[freeSlot] = parking[freeSlot], parking[targetSlot]
            
            # Target Slot is now available, simply move the car to target slot from current slot
            parking[targetSlot], parking[i] = parking[i], parking[targetSlot]

        return parking

s = Solution()

parking = [1, 0, -1]            # spots: 3 and cars: 2
print(s.parkingCars(parking))
parking = [3, 1, 2, 0, -1]      # spots: 5 and cars: 4
print(s.parkingCars(parking))
parking = [3, 5, 2, 0, 1, 4, -1]      # spots: 5 and cars: 4
print(s.parkingCars(parking))
