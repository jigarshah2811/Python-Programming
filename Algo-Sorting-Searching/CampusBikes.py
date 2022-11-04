class Solution(object):
    def campusBikes(self, workers, bikes):
        # Distance for all possible combinations
        distances = [(-1,-1,-1)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distances.append((distance, i, j))

        # Sort distances to start assigning bike-->worker with minimum distance
        distances.sort()


        # Assign bikes to worker. result[workerIndex] = bikeIndex
        results = [-1]*len(workers)
        usedBikes = dict()

        for distance, i, j in distances:
            if results[i] == -1 and j not in usedBikes:
                results[i] = j
                usedBikes[j] = True

        return results


s = Solution()
workers = [[0,0],[2,1]]
bikes = [[0,0],[2,1]]
print(s.campusBikes(workers, bikes))

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
print(s.campusBikes(workers, bikes))

