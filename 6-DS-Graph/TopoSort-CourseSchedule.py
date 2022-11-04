"""
https://leetcode.com/problems/course-schedule-ii/

"""
import collections
class Solution:
    def BuildGraph(self, numCourses, prerequisites):
        # Build Graph and INDEGREE for topological sorting
        self.numCourses = numCourses
        self.graph = collections.defaultdict(list)
        self.indegree = [0]*numCourses

        for course, revdep in prerequisites:
            self.graph[revdep].append(course)
            self.indegree[course] += 1
            
        print(f"Graph -->   {self.graph}")
        for i, val in enumerate(self.indegree):
            print(f"indegree[{i}] = {val}")

    def topoSort(self, numCourses, prerequisites):
        self.BuildGraph(numCourses, prerequisites)
        
        """ TOPOSORT: Keep finishing course that has indegree=0 (meaning no unfinished dependancies) """
        q = collections.deque()
        for course in range(self.numCourses):
            if self.indegree[course] == 0:  # This course has NO dependancies
                q.append(course)            # Queue up to finish
        
        res = []
        while q:    # Pop one-by-one course with NO dep and finish it
            course = q.popleft()    # This course is with indegree=0, so no dep
            res.append(course)
            for conn in self.graph[course]: # all courses that are UNBLOCKED due to this course is finish
                print(conn)
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:    # This course is READY to be finished
                    q.append(conn)

        # Check if ALL courses are finished
        if len(res) == self.numCourses:
            return res
        else:
            return []


s = Solution()
# numCourses = 5; prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3]]         #Output: [0, 1, 2, 3, 4] or [0, 2, 1, 3, 4] in that order
# print(s.topoSort(numCourses, prerequisites))

# numCourses = 5; prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3],[2,4]]   #Output: [] # Explanation: CYCLE between 2->4->2, 2,3,4 courses can't be completed
# print(s.topoSort(numCourses, prerequisites))

# numCourses = 2; prerequisites = [[1,0]]   #Output: [0, 1] # Explanation: 1 had dep on 0, so [0, 1]
# print(s.topoSort(numCourses, prerequisites))

# numCourses = 2; prerequisites = [[1,0],[0,1]]   #Output: [] # Explanation: CYCLE 1 had dep on 0, 0 has dep on 1 so neither can finish
# print(s.topoSort(numCourses, prerequisites))

numCourses = 2; prerequisites = [[0, 1]]   #Output: [0, 1] # Explanation: 1 had dep on 0, so [0, 1]
print(s.topoSort(numCourses, prerequisites))
