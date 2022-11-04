import collections, heapq, sys, re

class DinosorDataParser:
    def __init__(self) -> None:
        # We will make {DinosourName: [Len, Speed, Type]}   dictionary to build records
        self.recordsMap = collections.defaultdict(list)      
    def readFromFile(self, fileName: str) -> str:
        with open(fileName) as f:
            giantStr = f.read()
        return giantStr
    def parseDataUsingRegex(self, fileName):
        giantStr = self.readFromFile(fileName)

        """ REGEX: https://regex101.com/r/vfFHyc/1 """
        # Example: "DinosorName,DinosorLen,DinosorSpeed,DinosorType/Hadrosaurus,1.2,20,herbivore/ "
        # lines = re.findall(r"\w+,\d+.\d+,\d+,\w+", giantStr)

        # REGEX: GROUPS to extract using ([]@[]) format
        # Hadrosaurus,1.2,20,herbivore/
        lines = re.findall(r"(\w+),(\d+.\d+),(\d+),(\w+)\/", giantStr)
        print(lines)

        lines = lines[1:]
        for line in lines:
            records = line.split(",")
            dinosorName, dinosorLen, dinosorSpeed, dinosorType = records[0], records[1], records[2], records[3]
            try:
                self.recordsMap[dinosorName].extend([float(dinosorLen), int(dinosorSpeed), str(dinosorType)])
            except Exception as e:
                print(e)
                sys.exit(e)
        
        print(self.recordsMap)
        # Now Dict is Built, {str(DinosourName): [float(Len), int(Speed), str(Type)]}          
        for dName, vals in self.recordsMap.items():
            DinosorLen,DinosorSpeed,DinosorType = vals[0], vals[1], vals[2]
            print(f"{dName}\t{DinosorLen}\t{DinosorSpeed}\t{DinosorType}\n")
    def parseData(self, fileName: str):
        giantStr = self.readFromFile(fileName)
        
        # Sliding window to parse data, each line is seperated by "/" so that's END of 1 line
        start, end = 0, 0
        
        lineCount = 0
        for end, c in enumerate(giantStr):
            if c == "/":    
                if lineCount == 0:
                    # This is END of 1st line [start: end]
                    start = end + 1
                    lineCount += 1
                    continue

                # Parse all Records
                line = giantStr[start: end]
                records = line.split(",")       # header are seperated by ","  Example: "DinosorName,DinosorLen,DinosorType"
                DinosorName, DinosorLen,DinosorSpeed,DinosorType = records[0], records[1], records[2], records[3]
                self.recordsMap[DinosorName].extend([float(DinosorLen), int(DinosorSpeed), DinosorType])
                
                # Move window --->
                start = end+1
                lineCount += 1

        # Now Dict is Built, {str(DinosourName): [float(Len), int(Speed), str(Type)]}          
        print(f"{self.recordsMap}\n")
        for dName, vals in self.recordsMap.items():
            DinosorLen,DinosorSpeed,DinosorType = vals[0], vals[1], vals[2]
            print(f"{dName}\t{DinosorLen}\t{DinosorSpeed}\t{DinosorType}\n")

        # Filter: Print only TOP K Speed Dinosors
        topK = 3
        maxHeap = []
        for dName, vals in self.recordsMap.items():
            dLen,dSpeed,dType = vals[0], vals[1], vals[2]
            entry = [-1 * dSpeed, dName, dLen, dType]
            heapq.heappush(maxHeap, entry)
        print(f"MaxHeap: {maxHeap}")

        # Top K speed will be at the top, so pop and res
        print("\nDino\tSpeed")
        for _ in range(topK):
            entry = heapq.heappop(maxHeap)
            dSpeed, dName = (-1 * entry[0]), entry[1]
            print(f"{dName}\t| {dSpeed}")


s = DinosorDataParser()
s.parseDataUsingRegex("dinosours.csv")
# s.parseData("dinosours.csv")